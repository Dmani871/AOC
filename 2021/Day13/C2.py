import re

def main():
    instructions = []
    cords = set()

    with open('input.txt', 'r') as infile:
        for line in infile:
            if re.search("\d,\d", line):
                x, y = line.strip().split(",")
                cords.add((int(y),int(x)))
            else:
                instruction = re.search("([y,x]=\d+)", line)
                if instruction:
                    axis, pos = instruction.group(1).split("=")
                    axis = 1 if axis == 'x' else 0
                    instructions.append((axis, int(pos)))

    for instruction in instructions:
        old_cords = set()
        new_cords = set()
        for cord in cords:
            if cord[instruction[0]] > instruction[1]:
                new_pos = abs(cord[instruction[0]] - instruction[1] - instruction[1])
                new_cord = [0, 0]
                new_cord[instruction[0]] = new_pos
                new_cord[int(not instruction[0])] = cord[int(not instruction[0])]
                new_cords.add(tuple(new_cord))
                old_cords.add(cord)
        cords=cords-old_cords
        cords.update(new_cords)

    sorted_cords=sorted(cords)

    for index in range(len(sorted_cords)):
        if index>0:
            if sorted_cords[index][0] != sorted_cords[index-1][0]:
                print("")
            else:
                prev_x_diff=sorted_cords[index][1]-sorted_cords[index-1][1]

                print('.'*(prev_x_diff-1)*3, end='')
                print("#"*3,end='')


if __name__ == '__main__':
    main()
