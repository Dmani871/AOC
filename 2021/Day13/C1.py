import pandas as pd
import re


def main():
    instructions = []
    cords = set()
    with open('input.txt', 'r') as infile:
        for line in infile:
            if re.search("\d,\d", line):
                x, y = line.strip().split(",")
                cords.add((int(x), int(y)))
            else:
                instruction = re.search("([y,x]=\d+)", line)
                if instruction:
                    axis, pos = instruction.group(1).split("=")
                    axis = 0 if axis == 'x' else 1
                    instructions.append((axis, int(pos)))

    old_cords = set()
    new_cords = set()
    for cord in cords:
        if cord[instructions[0][0]] > instructions[0][1]:
            new_pos = abs(cord[instructions[0][0]] - instructions[0][1] - instructions[0][1])
            new_cord = [0, 0]
            new_cord[instructions[0][0]] = new_pos
            new_cord[int(not instructions[0][0])] = cord[int(not instructions[0][0])]
            new_cords.add(tuple(new_cord))
            old_cords.add(cord)
    cords=cords-old_cords
    cords.update(new_cords)
    return len(cords)




if __name__ == '__main__':
    print(main())
