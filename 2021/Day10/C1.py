from collections import Counter


def main():
    bracket_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    opening_brackets = set(bracket_pairs.keys())
    point_mapping = dict(zip(bracket_pairs.values(), [3, 57, 1197, 25137]))
    points = 0
    with open('input.txt', 'r') as infile:
        for line in infile:
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
                        points += point_mapping[bracket]
                        break
                index += 1
        return points


if __name__ == '__main__':
    print(main())
