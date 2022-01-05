import re
 
with open('instructions.txt') as file:
    instructions=[]
    iid=0
    for line in file:
        instruction=re.search(r'([a-zA-Z]+) (([+]|[-])[0-9]+)',line)
        instructions.append([instruction.group(1),int(instruction.group(2)),iid])
        iid+=1
    

def attempt(instructions):
    acc=0
    counter=0
    called=[]
    while counter<len(instructions):
        i=instructions[counter]
        if i[2] in called:
            return False
        elif i[0]=='nop':
            counter+=1
        elif i[0]=='acc':
            acc+=i[1]
            counter+=1
        elif i[0]=='jmp':
            counter+=i[1]
        called.append(i[2])
    return acc

for x in instructions:
    temp=x[0]
    if x[0]=='nop':
        x[0]='jmp'
    else:
        x[0]='nop'
    c=attempt(instructions)
    if c==False:
        x[0]=temp
    else:
        print(c)
        break