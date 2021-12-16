import pandas as pd
import numpy as np
from io import StringIO


def bingo():
    with open('input.txt', 'r') as infile:
        data = [item for item in infile]
        # convert the first line of the file into the bingo numbers
        bingo_numbers = data[0].strip().split(",")
        # read the remaining grids left in the file
        df = pd.read_csv(StringIO(''.join(line for line in data[1:])), delimiter="\n", names=["grids"], dtype=str)
        # expand grids so that each number in the grid can be referenced
        bingo_grids = df["grids"].str.split(expand=True)
        # stores the first row of the winning grid
        winning_grid = None
        # stores the bingo number the grid one one.
        winning_bingo_number = None
        # boolean to track if any grid is complete
        is_last_complete_grid = False
        # start crossing of the bingo numbers
        for bingo_number in bingo_numbers:
            # if the last complete grid is found stop
            if is_last_complete_grid:
                break
            # mark the bingo numbers by replacing it with the N/A string
            bingo_grids = bingo_grids.replace(bingo_number, "N/A")
            # select all the rows that only have N/A in it
            complete_rows = np.where((bingo_grids == "N/A").all(axis=1))[0]
            if complete_rows.size > 0:
                winning_bingo_number = bingo_number
                # for all rows completed rows remove thier grid
                for row in complete_rows:
                    winning_grid = row - row % 5
                    if len(bingo_grids) == 5:
                        is_last_complete_grid = True
                        break
                    else:
                        bingo_grids = bingo_grids.drop(range(winning_grid, winning_grid + 5))
                # after all dropping the winning grids reset index
                bingo_grids.reset_index(drop=True, inplace=True)

            columns_of_intrest = np.where((bingo_grids == "N/A") == True)
            grid_starting_rows = [row - (row % 5) for row in columns_of_intrest[0]]
            coordinates = set(zip(grid_starting_rows, columns_of_intrest[1]))
            for cord in coordinates:
                grid_start = cord[0]
                complete_col = set(bingo_grids.iloc[grid_start:grid_start + 5, cord[1]]) == {'N/A'}
                if complete_col:
                    winning_grid = grid_start
                    winning_bingo_number = bingo_number
                    if len(bingo_grids) == 5:
                        is_last_complete_grid = True
                        break
                    else:
                        bingo_grids.drop(range(winning_grid, winning_grid + 5),inplace=True)
                        bingo_grids.reset_index(drop=True, inplace=True)

        # select the winning grid
        winning_grid = bingo_grids.iloc[winning_grid:winning_grid + 5, 0:5]
        # replace all the marked bingo numbers with 0
        winning_grid = winning_grid.replace("N/A", "0")
        # turn grid into ints
        winning_grid = winning_grid.astype(int)
        # TODO:sum using previous bingo numbers
        # gets the sum of each col and adds them up
        remaining_total = sum(winning_grid.sum(axis=0).tolist())
        return remaining_total * int(winning_bingo_number)


if __name__ == '__main__':
    print(bingo())
