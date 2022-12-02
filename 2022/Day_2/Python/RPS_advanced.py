point_mapping = {'A':1,'B':2,'C':3}
wining_combinations=[('C','A'),('B','C'),('A','B')]
def score(input_tuple):
    if any(input_tuple == item for item in wining_combinations):
        return 6
    elif input_tuple[1]==input_tuple[0]:
        return 3
    else:
        return 0
total=0
def get_losing_comb(c):
    for comb in wining_combinations:
        if comb[0]==c:
            return comb
with open("strategy.txt") as cal_file:
    for line in cal_file:
        i1,i2=line.split()
        sn=''
        if i2=='Y':
            sn=i1
        else:
            comb=get_losing_comb(i1)
            if i2=='Z':
                sn=comb[1]
            else:
                sn="ABC".replace(i1, "").replace(comb[1], "")
        total+=score((i1,sn)) 
        total+=point_mapping[sn]
print(total)