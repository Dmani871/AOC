from collections import defaultdict,Counter


def find_paths(start, connection_map, visited_small_caves):
    if start == 'end':
        return 1
    paths = 0
    if start.islower():
        visited_small_caves.append(start)
    start_length=len(visited_small_caves)
    for cave in connection_map[start]:
        small_caves_count = Counter(visited_small_caves)
        if (cave.islower() and (cave not in visited_small_caves or max(small_caves_count.values())<2)) or cave.isupper():
            paths += find_paths(cave, connection_map, visited_small_caves)
        visited_small_caves=visited_small_caves[:start_length]
    return paths


def main():
    connection_map = defaultdict(list)
    with open('input.txt', 'r') as infile:
        for connection in infile:
            cave1, cave2 = connection.strip().split("-")
            if cave2 != "start":
                connection_map[cave1].append(cave2)
            if cave1 != "start":
                connection_map[cave2].append(cave1)
        del connection_map['end']
        return find_paths('start', connection_map, [])


if __name__ == '__main__':
    print(main())
