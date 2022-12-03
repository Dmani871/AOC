import string
letters=list(string.ascii_letters)
s=0
with open("Inputs/day3.txt", "r") as f:
    for pack in f:
        middle_index = len(pack)//2
        duplicate_char=set(pack[:middle_index]).intersection(set(pack[middle_index:]))
        s+=letters.index(duplicate_char.pop())+1
print(s)