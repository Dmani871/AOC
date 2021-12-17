import pandas as pd

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
    low_points=[]
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
                low_points.append(current_value)
    # retuns the sum of all the low points plus 1
    return sum(map(lambda x:x+1,low_points))


if __name__ == '__main__':
    print(lava())
