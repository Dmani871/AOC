import pandas as pd
from collections import defaultdict
#TODO:Check how pass by ref works with df
def find_basin(start,visted,df):
    col,row=start
    visted.add(start)
    adjacent_cords=set()
    for index_add in [1, -1]:
        adjacent_cords.add((col,row + index_add))
        adjacent_cords.add((col+index_add, row))
    for cord in adjacent_cords-visted:
        col, row = cord
        if df.iloc[row,col]!=9:
            find_basin((col,row), visted, df)




def lava():
    # read in the values
    df = pd.read_csv('input.txt', delimiter="\n",names=["grid"],dtype = str)
    # expand the grids into cols
    df=df['grid'].str.split('',expand=True)
    #pad all around grid with 9's
    df.loc[len(df)]=df.loc[-1]=df[0]=df[(df.columns)[-1]]=9
    # reset indexes
    df.index=df.index+1
    df.sort_index(inplace=True)
    # convert to ints
    df=df.astype(int)
    # holds all the found lowpoints
    low_points=defaultdict(set)
    for col in range(1, len(df.columns) - 1):
        for row in range(1,len(df)-1):
            # holds the set of all adjacent values of the current value
            adjacent_values=set()
            current_value=df.iloc[row,col]
            for index_add in [1,-1]:
                # adds vertical adjacents
                adjacent_values.add(df.iloc[row+index_add,col])
                # adds horizontal adjacents
                adjacent_values.add(df.iloc[row , col+index_add])
            # if the lowest adjacent is greater than the current value then it is a low point
            if current_value<min(adjacent_values):
                low_points[(col,row)].add((col,row))
    basin_sizes=[]
    for point in low_points:
        find_basin(point,low_points[point],df)
        basin_sizes.append(len(low_points[point]))
    basin_sizes=sorted(basin_sizes)
    return basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]

if __name__ == '__main__':
    print(lava())
