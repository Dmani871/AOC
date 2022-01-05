with open('map.txt') as file:
    x=0
    no_of_tree=0
    for line in file:
        line=line.rstrip()
        while x>len(line):
            line=line+line
        if line[x]=="#":
            no_of_tree+=1
        x=x+3
    print(no_of_tree)