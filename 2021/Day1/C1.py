
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

if __name__ == '__main__':
    print(simple())
