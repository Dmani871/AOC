import math


def crabs():
    with open('input.txt', 'r') as infile:
        data = infile.read().rstrip()
        crabs_data= list(map(int, data.split(',')))
        cords_range=range(min(crabs_data),max(crabs_data))
        lowest_feul_cost=math.inf
        for cord in cords_range:
            feul_cost=sum(map(lambda x : abs(cord-x),crabs_data))
            lowest_feul_cost=min(feul_cost,lowest_feul_cost)
        return lowest_feul_cost


if __name__ == '__main__':
    print(crabs())
