from collections import namedtuple
import operator
from functools import reduce
Packet = namedtuple('Packet', ['end_index', 'data'])
Header = namedtuple('Header', ['start_index', 'end_index'])
LITERAL_PACKET_TYPE_ID = 4
LITERAL_GROUP_LEN = 5
END_GROUP_BIT_INDEX = 0
VERSION_NUM_HEADER = Header(start_index=0, end_index=3)
PACKET_TYPE_HEADER = Header(start_index=3, end_index=6)
LEN_TYPE_HEADER = Header(start_index=6, end_index=7)
DATA_START_INDEX = 7
TYPE_0_LEN_BITS = 15
TYPE_1_LEN_BITS = 11
OPERATIONS = {
    0: lambda operands: sum(operands),
    1: lambda operands: reduce(operator.mul,operands),
    2: lambda operands: min(operands),
    3: lambda operands: max(operands),
    5: lambda operands: int(operands[0]>operands[1]),
    6: lambda operands: int(operands[0]<operands[1]),
    7: lambda operands: int(operands[0]==operands[1]),
}

def decode(bin_string):
    packet_type_id = int(bin_string[PACKET_TYPE_HEADER.start_index:PACKET_TYPE_HEADER.end_index], 2)
    if packet_type_id == LITERAL_PACKET_TYPE_ID:
        is_end = False
        pk_binary_string = ""
        start = PACKET_TYPE_HEADER.end_index
        end = start + LITERAL_GROUP_LEN
        while not is_end and end <= len(bin_string):
            group = bin_string[start:end]
            if group[END_GROUP_BIT_INDEX] == '0':
                is_end = True
            pk_binary_string += str(group[1:])
            start = end
            end = start + LITERAL_GROUP_LEN
        return Packet(end_index=start, data=int(pk_binary_string,2))
    else:
        length_type_id = int(bin_string[LEN_TYPE_HEADER.start_index:LEN_TYPE_HEADER.end_index])
        length_type_bits = TYPE_1_LEN_BITS if length_type_id else TYPE_0_LEN_BITS
        no_of_bits_length = LEN_TYPE_HEADER.end_index + length_type_bits
        sub_packet_length = int(bin_string[DATA_START_INDEX:no_of_bits_length], 2)
        remaining_bits = sub_packet_length
        start_index = no_of_bits_length
        operands=[]
        while remaining_bits > 0:
            packet_info = decode(bin_string[start_index:])
            remaining_bits -= 1 if length_type_id else packet_info.end_index
            start_index += packet_info.end_index
            operands.append(packet_info.data)
        result=OPERATIONS[packet_type_id](operands)
        return Packet(end_index=start_index, data=result)


def main():
    sums = []
    with open('input.txt', 'r') as infile:
        for hex_string in infile:
            binary_sting = ''.join('{0:04b}'.format(int(encoding, 16)) for encoding in hex_string.rstrip())
            sums.append(decode(binary_sting).data)
    return sum(sums)


if __name__ == '__main__':
    print(main())
