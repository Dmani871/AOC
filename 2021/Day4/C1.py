import pandas as pd
import numpy as np
from io import StringIO
def bingo():
    with open('input.txt', 'r') as infile:
        data=[item for item in infile]
        bingo_numbers=data[0].strip().split(",")
        df = pd.read_csv(StringIO(''.join(line for line in data[1:])), delimiter="\n", names=["grids"], dtype=str)
        bingo_grids = df["grids"].str.split(expand=True)
        winning_grid=None
        winning_bingo_number=None
        is_bingo=False
        for bingo_number in bingo_numbers:
            if(is_bingo):
                break
            bingo_grids=bingo_grids.replace(bingo_number,"N/A")
            complete_rows=np.where((bingo_grids == "N/A").all(axis=1))[0]
            # assumption that only one person wins at this type of bingo
            if(complete_rows.size==1):
                winning_grid=complete_rows[0]-complete_rows[0]%5
                winning_bingo_number=bingo_number
                is_bingo=True
                break
            columns_of_intrest=np.where((bingo_grids == "N/A") == True)
            grid_starting_rows=[row-(row%5) for row in columns_of_intrest[0]]
            coordinates=set(zip(grid_starting_rows,columns_of_intrest[1]))
            for cord in coordinates:
                grid_start=cord[0]
                complete_col=set(bingo_grids.iloc[grid_start:grid_start+5, cord[1]])=={'N/A'}
                if (complete_col) and not is_bingo:
                    is_bingo=True
                    winning_grid=grid_start
                    winning_bingo_number = bingo_number
                    break

        winning_grid=bingo_grids.iloc[winning_grid:winning_grid+5,0:5]
        winning_grid=winning_grid.replace("N/A","0")
        winning_grid=winning_grid.astype(int)
        print(winning_grid)
        #TODO:sum using previous bingo numbers
        remaining_total=sum(winning_grid.sum(axis=0).tolist())
        return remaining_total * int(winning_bingo_number)

if __name__ == '__main__':
    print(bingo())
