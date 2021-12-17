from collections import defaultdict, Counter
import string


def displays():
    values=[]
    digit_mappings = {'abcefg': '0',
                      'cf': '1',
                      'acdeg': '2',
                      'acdfg': '3',
                      'bcdf': '4',
                      'abdfg': '5',
                      'abdefg': '6',
                      'acf': '7', 'abcdefg': '8',
                      'abcdfg': '9'}
    with open('input.txt', 'r') as infile:
        data = [line.rstrip().split('|') for line in infile]
        for entry in data:
            output_values = defaultdict(Counter)
            signal_mappings = defaultdict(None)
            for pattern in entry[0].split():
                output_values[len(pattern)].update(list(pattern))

            signal_mappings['a'], *_ = set(output_values[3].keys()) - set(output_values[2].keys())
            b_and_d = set(output_values[4].keys()) - set(output_values[3].keys())
            most_common = set([x for x, count in output_values[5].items() if count == 3])
            signal_mappings['d'], *_ = most_common.intersection(b_and_d)
            signal_mappings['b'], *_ = b_and_d - set(signal_mappings['d'])
            signal_mappings['g'], *_ = most_common - set(signal_mappings.values())
            least_common = set([x for x, count in output_values[6].items() if count == 2])
            c_and_e = least_common - set(signal_mappings.values())
            signal_mappings['c'], *_ = c_and_e.intersection(set(output_values[2].keys()))
            signal_mappings['e'], *_ = c_and_e - set(signal_mappings['c'])
            signal_mappings['f'], *_ = set(output_values[7].keys()) - set(signal_mappings.values())
            signal_mappings = {value: key for key, value in signal_mappings.items()}

            output_string=""
            for pattern in entry[1].split():
                mapped_pattern=list(map(lambda s:signal_mappings[s],pattern))
                output_string+=digit_mappings[''.join(sorted(mapped_pattern))]
            values.append(int(output_string))
        return  sum(values)


if __name__ == '__main__':
    print(displays())
