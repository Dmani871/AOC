from collections import namedtuple, defaultdict
from itertools import cycle


def vents():
    grid = defaultdict(int)
    Vent = namedtuple("Vent", ["x1", "y1", "x2", "y2"])

    with open('input.txt', 'r') as infile:
        for item in infile:
            item = item.replace("->", ",").strip()
            vent = Vent(*list(map(int, item.split(','))))
            x_step = 1 if vent.x1 < vent.x2 else -1
            y_step = 1 if vent.y1 < vent.y2 else -1
            vent_x_cords = range(vent.x1, vent.x2 + x_step, x_step)
            vent_y_cords = range(vent.y1, vent.y2 + y_step, y_step)
            cords = zip(vent_x_cords, cycle(vent_y_cords)) if len(vent_y_cords) < len(vent_x_cords) else zip(
                cycle(vent_x_cords), vent_y_cords)
            for cord in cords:
                grid[str(cord[0]) + "," + str(cord[1])] += 1
        return sum(map(lambda x: x > 1, grid.values()))


if __name__ == '__main__':
    print(vents())
