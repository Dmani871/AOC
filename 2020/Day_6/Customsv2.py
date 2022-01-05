from collections import Counter
with open('questions.txt') as file:
    count=0
    people_count=0
    group=''
    for line in file:
        if line=='\n':
            yes_counts=Counter(list(group)).values()
            count+=(list(yes_counts).count(people_count))
            group=''
            people_count=0

        else:
            group+=line.strip()
            people_count+=1
print(count)