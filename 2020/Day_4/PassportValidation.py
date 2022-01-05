import re
import pandas as pd
required_fields={
    'byr':r'byr:\b(19[2-9][0-9]|200[0-2])\b\s', 
    'iyr':r'iyr:\b(201[0-9]|2020)\b\s',
    'eyr':r'eyr:\b(202[0-9]|2030)\b\s', 
    'hgt':r'hgt:(\b(1[5-8][0-9]|19[0-3])cm\b|\b(59|6[0-9]|7[0-6])in\b)\s', 
    'pid':r'pid:([0-9]{9})\s',
    'ecl':r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\s',
    'hcl':r'hcl:(#[0-9a-f]{6})\s'
}

no_of_valid_passports=0
with open ('passports.txt') as file:
    passport_info=''
    for line in file:
        if line == "\n" :
            valid_passport=True
            for k in required_fields:
                match=re.search(required_fields[k],passport_info)
                if match==None:
                    valid_passport=False
                    break
            if valid_passport:
                no_of_valid_passports+=1
            passport_info=''
        else:
            passport_info=passport_info+line+" "

print(no_of_valid_passports)