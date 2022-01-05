
with open('questions.txt') as file:
    count=0
    group=''
    for line in file:
        if line=='\n':
            count+=len(set(group))
            group=''

        else:
            group+=line.strip()
print(count)