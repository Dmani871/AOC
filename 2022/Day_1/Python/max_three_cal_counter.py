total_cals=[]
cals=0
with open("cals.txt") as cal_file:
    for line in cal_file:
        if line.strip().isdigit():
            cals+=int(line)
        else:
            total_cals.append(cals)
            cals=0
print(sum(sorted(total_cals)[-3:]))