import re

def check_valid_pwd(filename,pwdregex):
    valid_password=0
    with open(filename) as file:
        for line in file:
            line="".join(line.split())
            match = re.search(pwdregex,line)
            if match !=None:
                count=match.group(4).count(match.group(3))
                if count>=int(match.group(1)) and count<=int(match.group(2)):
                    valid_password+=1
    return valid_password
 
print(check_valid_pwd('passwds.txt','([0-9]+)-([0-9]+)([a-zA-Z]):([\w]+)'))