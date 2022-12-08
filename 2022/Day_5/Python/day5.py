import re
from copy import deepcopy
from collections import defaultdict
stacks=defaultdict(list)
instructions=[]
def mover(in_stacks_dict,reverse=True):
    stacks_dict=deepcopy(in_stacks_dict)
    for i in instructions:
        to_move=stacks_dict[i[1]][-i[0]:]
        if reverse:
            to_move.reverse()
        stacks_dict[i[2]].extend(to_move)
        stacks_dict[i[1]]=stacks_dict[i[1]][:-i[0]]
    return stacks_dict
def print_stacks_end(stacks_dict):
    for k in sorted(stacks_dict.keys()):
        if stacks_dict[k]:
            print(stacks_dict[k][-1],end='')
    print()
stack_regex = re.compile("[A-Z]")
with open("Inputs/day5.txt", "r") as f:
    for line in f:
        intruction_regex = re.search("move ([\d]+) from ([\d]+) to ([\d]+)",line.strip("\n"))
        if intruction_regex:
            tuple_of_integers = tuple(map(int, intruction_regex.groups()))
            instructions.append(tuple_of_integers)
        else:
            for m in stack_regex.finditer(line.strip("\n")):
                stacks[m.start()].insert(0, m.group())
nstacks=defaultdict(list)
for ind,k in enumerate(sorted(stacks.keys()),start=1):
    nstacks[ind]=stacks[k]

S1=mover(nstacks)
S2=mover(nstacks,False)
print_stacks_end(S1)
print_stacks_end(S2)
