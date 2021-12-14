import pandas as pd
import numpy as np
def simple():
    increased_count=0
    with open("input.txt") as depth_readings: 
        depths = map(int,depth_readings.readlines())
        print(depths)
        previousMeasurement = None
        for currentMeasurement in depths:
            if (previousMeasurement!=None)and(currentMeasurement> previousMeasurement) :
                increased_count+=1
            previousMeasurement=currentMeasurement
    return increased_count

def complex():
    df = pd.read_csv('input.txt', delimiter="\n",names=["depths"])
    diffs=np.ediff1d(df['depths'].values, to_begin=0)
    return (0<diffs).sum()

if __name__ == '__main__':
    print(simple())
    print(complex())
