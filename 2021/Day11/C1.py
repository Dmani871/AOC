import pandas as pd
import numpy as np
from itertools import product


def main():
    # read in the values
    df = pd.read_csv('input.txt', delimiter="\n", names=["grid"], dtype=str)
    # expand the grids into cols
    df = df['grid'].str.split('', expand=True)
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    MAX_X = MAX_Y = 10
    MIN_X = MIN_Y = 0
    df.columns = range(MIN_X, MAX_X)
    # convert to ints
    df = df.astype(int)
    steps = 0
    total_flashes = 0

    while steps < 100:
        df = df + 1
        flashed = set()
        while True:
            flashes = np.where((df > 9))
            flashes = set(zip(flashes[0], flashes[1])) - flashed
            if len(flashes) == 0:
                total_flashes += len(flashed)
                for cord in flashed:
                    df.iloc[cord[0], cord[1]] = 0
                break
            else:
                for cord in flashes:
                    flashed.add(cord)
                    y, x = cord
                    adjacent_cords = product(range(max(x - 1, MIN_X), min(x + 2, MAX_X)),
                                             range(max(y - 1, MIN_Y), min(y + 2, MAX_Y)))
                    for adjacent_cord in adjacent_cords:
                        df.iloc[adjacent_cord[1], adjacent_cord[0]] += 1

        steps+=1
    print(total_flashes)


if __name__ == '__main__':
    print(main())
