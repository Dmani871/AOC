import re

def check_valid_pwd(filename,pwdregex):
    valid_password=0
    with open(filename) as file:
        for line in file:
            line="".join(line.split())
            match = re.search(pwdregex,line)
            if match !=None:
                word=match.group(4)
                letter=match.group(3)
                first_index_bool=word[int(match.group(1))-1]==letter
                second_index_bool=word[int(match.group(2))-1]==letter
                if first_index_bool != second_index_bool:
                    valid_password+=1
    return valid_password
 
print(check_valid_pwd('passwds.txt','([0-9]+)-([0-9]+)([a-zA-Z]):([\w]+)'))