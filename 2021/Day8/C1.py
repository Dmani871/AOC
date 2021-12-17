from collections import defaultdict


def displays():
    digit_mappings=defaultdict(int,{2:1,4:4,3:7,7:8})
    output_values=defaultdict(int)
    with open('input.txt', 'r') as infile:
        data = [line.rstrip().split('|') for line in infile]
        for entry in data:
            output_signals=entry[1].split()
            for digit in output_signals:
                output_values[digit_mappings[len(digit)]]+=1
        return sum([output_values[x] for x in [1,4,7,8]])

if __name__ == '__main__':
    print(displays())
