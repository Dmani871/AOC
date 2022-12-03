import string
letters=list(string.ascii_letters)
s=0
with open("Inputs/day3.txt", "r") as f:
    badge=set()
    for x,pack in enumerate(f):
        if x%3==0:
            try:
                s+=letters.index(badge.pop())+1
            except KeyError:
                pass
            badge=set(pack.strip())
        badge=badge.intersection(set(pack.strip()))
s+=letters.index(badge.pop())+1
print(s)