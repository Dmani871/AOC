import re
from collections import  defaultdict,Counter
def main():
    insertion_pairs=defaultdict(str)
    polymer=[]
    insertion_regex="([A-Z]{2}) -> ([A-Z])"
    with open('input.txt', 'r') as infile:
        for line in infile:
            is_insertion=re.search(insertion_regex,line.strip())
            if is_insertion is not None:
                insertion_pairs[is_insertion.group(1)]=is_insertion.group(2)
            else:
                polymer.extend(list(line.strip()))

    steps=0
    while steps<10:
        inserts=defaultdict(str)
        for index in range(len(polymer)-1):
            inserts[index+1]=insertion_pairs[polymer[index]+polymer[index+1]]
        no_insert=0
        for insert_index in inserts:
            polymer.insert(insert_index+no_insert,inserts[insert_index])
            no_insert+=1
        steps+=1
    polymer_counter=Counter(polymer)
    polymer_counter_vals=polymer_counter.values()
    return (max(polymer_counter_vals)) - (min(polymer_counter_vals))







if __name__ == '__main__':
    print(main())
