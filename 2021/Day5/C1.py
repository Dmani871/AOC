from collections import namedtuple, defaultdict
from functools import reduce


def vents():
    grid = defaultdict(int)
    Vent = namedtuple("Vent", ["x1", "y1", "x2", "y2"])
    horizontal_vents = []
    vertical_vents = []

    with open('input.txt', 'r') as infile:
        for item in infile:
            item = item.replace("->", ",").strip()
            v = Vent(*list(map(int, item.split(','))))
            if v.x1 == v.x2:
                vertical_vents.append(v)
            elif v.y1 == v.y2:
                horizontal_vents.append(v)
        for vent in horizontal_vents:
            vent_x_cords = list(range(min(vent.x1, vent.x2), max(vent.x1, vent.x2) + 1))
            for x in vent_x_cords:
                grid[str(x) + "," + str(vent.y1)] += 1
        for vent in vertical_vents:
            vent_y_cords = list(range(min(vent.y1, vent.y2), max(vent.y1, vent.y2) + 1))
            for y in vent_y_cords:
                grid[str(vent.x1) + "," + str(y)] += 1
        return sum(map(lambda x: x > 1, grid.values()))


if __name__ == '__main__':
    print(vents())
