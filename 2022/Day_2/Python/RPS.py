point_mapping = {'X':1,'Y':2,'Z':3}
encryption_mapping ={'A':'X','B':'Y','C':'Z'}
wining_combinations=[('Z','X'),('Y','Z'),('X','Y')]
def score(input_tuple):
    if any(input_tuple == item for item in wining_combinations):
        return 6
    elif input_tuple[1]==input_tuple[0]:
        return 3
    else:
        return 0
total=0
with open("strategy.txt") as cal_file:
    for line in cal_file:
        i1,i2=line.split()
        total+=score((encryption_mapping[i1],i2))
        total+=point_mapping[i2]
print(total)