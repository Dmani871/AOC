from collections import defaultdict


def find_paths(start, connection_map, visited):
    if start == 'end':
        return 1
    paths = 0
    visited.append(start)
    start_length=len(visited)
    for cave in connection_map[start]:
        if (cave.islower() and cave not in visited) or cave.isupper():
            paths += find_paths(cave, connection_map, visited)
        visited=visited[:start_length]
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
