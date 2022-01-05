import re

with open('rules.txt') as file:
    bag_rules={}
    for line in file:
        bag=re.search(r'([\w]+\s[\w]+) bags',line)
        contents=re.findall(r'\d ([\w]+\s[\w]+)',line)
        bag_rules[bag.group(1)]=contents

def search_bag(values,rules):
    if values==[]:
        return 0
    elif 'shiny gold' in values:
        return 1
    else:
        results=[]
        for bag in values:
            results.append(search_bag(rules[bag],rules))
        return max(results)

count=0
for k,v in bag_rules.items():
    count+=search_bag(v,bag_rules)
print(count)


