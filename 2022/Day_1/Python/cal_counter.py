cals=0
max_cal=0
with open("cals.txt") as cal_file:
    for line in cal_file:
        if line.strip().isdigit():
            cals+=int(line)
            max_cal=cals if cals>max_cal else max_cal
        else:
            cals=0
print(max_cal)
