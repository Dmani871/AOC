from collections import namedtuple, defaultdict
from functools import reduce


def lanternfish():
    with open('input.txt', 'r') as infile:
        day=0
        data = infile.read().rstrip()
        lanternfish_data = list(map(int, data.split(',')))
        while day <80:
            for fish_index in range(len(lanternfish_data)):
                if lanternfish_data[fish_index] == 0:
                    lanternfish_data[fish_index]=6
                    lanternfish_data.append(8)
                else:
                    lanternfish_data[fish_index] -=1
            day+=1
        return len(lanternfish_data)


if __name__ == '__main__':
    print(lanternfish())
