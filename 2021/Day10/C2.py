
def main():
    bracket_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    opening_brackets = set(bracket_pairs.keys())
    point_mapping = dict(zip(bracket_pairs.values(), range(1,5)))
    total_points = []
    with open('input.txt', 'r') as infile:
        for line in infile:
            points=0
            incomplete=True
            stack = []
            c = (list(line.rstrip()))
            index = 0
            while index < len(c):
                bracket = c[index]
                if bracket in opening_brackets:
                    stack.append(bracket)
                else:
                    expected_closing_bracket = bracket_pairs[stack.pop()]
                    if expected_closing_bracket != bracket:
                        incomplete=False
                        break
                index += 1
            if(incomplete):
                while len(stack)!=0:
                    points*=5
                    points += point_mapping[bracket_pairs[stack.pop()]]
                total_points.append(points)
    middleIndex = int((len(total_points) - 1) / 2)
    return sorted(total_points)[middleIndex]



if __name__ == '__main__':
    print(main())
