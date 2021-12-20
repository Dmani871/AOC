import re
import math
from collections import defaultdict


# TODO:Refactor
def get_neighbors(cords):
    x, y = cords
    adjacent_cords = set()
    for index_add in [1, -1]:
        adjacent_cords.add((x + index_add, y))
        adjacent_cords.add((x, y + index_add))
    return adjacent_cords


def main():
    graph = {}
    with open('input.txt', 'r') as infile:
        y = 0
        for line in infile:
            x = 0
            for chiton in map(int, re.findall("\d", line)):
                graph[x, y] = [chiton, math.inf, None]
                x += 1
            y += 1
    MAX_X = x
    MAX_Y = y

    x_mappings = list(map(lambda i: i * MAX_X, range(1, 5)))
    y_mappings = list(map(lambda i: i * MAX_Y, range(1, 5)))

    original_keys = list(graph.keys())
    for key in original_keys:
        x, y = key
        x_index = 1
        for mapping in x_mappings:
            graph[x + mapping, y] = graph[key].copy()
            graph[x + mapping, y][0] = round((graph[x + mapping, y][0] + x_index) % 9.1)
            x_index += 1
        MAX_X=x + mapping
    updated_keys = list(graph.keys())
    for key in updated_keys:
        x, y = key
        y_index = 1
        for mapping in y_mappings:
            graph[x, y + mapping] = graph[key].copy()
            graph[x, y + mapping][0] = round((graph[x, y + mapping][0] + y_index )% 9.1)
            y_index += 1
        MAX_Y=y + mapping
    priority_q=defaultdict(list)
    priority_q[math.inf].extend(graph.keys())
    priority_q[math.inf].remove((0,0))
    priority_q[0].append((0,0))
    graph[0, 0][1] = 0
    while priority_q:
        for key in sorted(priority_q):
            for cord in priority_q[key]:
                current_node_val = graph[cord][1]
                for neighbor in get_neighbors(cord):
                    try:
                        cost = current_node_val + graph[neighbor][0]
                        if cost < graph[neighbor][1]:
                            graph[neighbor][1] = cost
                            graph[neighbor][2] = cord
                            priority_q[cost].append(neighbor)
                    except KeyError:
                        pass
            del priority_q[key]
    return graph[MAX_X,MAX_Y][1]





if __name__ == '__main__':
    print(main())
