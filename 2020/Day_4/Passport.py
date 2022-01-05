import re
required_fields={'ecl', 'hgt', 'pid', 'hcl', 'byr', 'eyr', 'iyr'}
no_of_valid_passports=0
no_of_passport=0
no_of_invalid_passports=0
with open ('passports.txt') as file:
    passport_info=''
    for line in file:
        if line == "\n" :
            info_items=[]
            passport_info=passport_info.split()
            for info in passport_info:
                match =re.search('([\w]+):(.+)',info)
                info_items.append(match.group(1))
            info_items=set(info_items)
            info_items.discard('cid')
            if not bool(required_fields-info_items):
                no_of_valid_passports+=1
            if bool(required_fields-info_items):
                no_of_invalid_passports+=1
            no_of_passport+=1
            passport_info=''
        else:
            passport_info=passport_info+line
print(no_of_valid_passports)
print(no_of_passport)
print(no_of_invalid_passports)