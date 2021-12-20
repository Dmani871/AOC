import re
import math

#TODO:Refactor
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
    unvisited_nodes = list(reversed((graph.keys())))
    visited_nodes = set()
    graph[0, 0][1] = 0
    while len(visited_nodes) != len(graph):
        current_node = unvisited_nodes.pop()
        current_node_val = graph[current_node][1]
        for neighbor in get_neighbors(current_node):
            try:
                cost=current_node_val + graph[neighbor][0]
                if cost < graph[neighbor][1]:
                    graph[neighbor][1] = cost
                    graph[neighbor][2] = current_node
            except KeyError:
                pass
        unvisited_nodes.sort(reverse=True, key=lambda x:graph[x][1])
        visited_nodes.add(current_node)
    return graph[x-1,y-1][1]


if __name__ == '__main__':
    print(main())
