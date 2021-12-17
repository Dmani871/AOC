from collections import namedtuple, defaultdict
from functools import reduce

from collections import defaultdict
def lanternfish():
    with open('input.txt', 'r') as infile:
        days=1
        data = infile.read().rstrip()
        lanternfish_data = list(map(int, data.split(',')))
        fish_days=dict.fromkeys(range(0,9), 0)

        for fish in lanternfish_data:
             fish_days[fish]+=1
        while (days<=256):
            # the number of new fish is the number of 0's
            no_of_new_fish=fish_days[0]
            # holds the previous count of the 1 infront of it
            previous=fish_days[8]
            # shift
            for key in reversed(range(0,8)):
                temp=fish_days[key]
                fish_days[key]=previous
                previous=temp
            # after shift add the number of 0's to 6's
            fish_days[6]+=no_of_new_fish
            # after shift then the number of 8 should be 0 so add new fish
            fish_days[8]=no_of_new_fish
            days+=1
        return sum(fish_days.values())



if __name__ == '__main__':
    print(lanternfish())
