import re

with open('rules.txt') as file:
    bag_rules={}
    for line in file:
        bag=re.search(r'([\w]+\s[\w]+) bags',line)
        contents=re.findall(r'(\d) ([\w]+\s[\w]+)',line)
        bag_rules[bag.group(1)]=contents

def search_bag(values,b):
    if values==[]:
        return 1
    else:
        count=0
        for bag in values:
            count+=int(bag[0])*(search_bag(b[bag[1]],b))
        count=count+1
        return count


print(search_bag(bag_rules['shiny gold'],bag_rules)-1)