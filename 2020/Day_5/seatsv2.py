import math
def seat_range(boarding_pass,start,end,upper,lower):
    if boarding_pass!=[]:
        char=boarding_pass.pop(0)
        diff=end-start
        if char==lower:
            end=math.floor(end-(diff)/2)
        elif char==upper:
            start=math.ceil(start+(diff)/2)
        return seat_range(boarding_pass,start,end,upper,lower)
    else:
        return end

with open('boardingpasses.txt') as file:
    seat_ids=[]
    possible_seats=[]
    for line in file:
        boarding_pass=list(line)
        row=seat_range(boarding_pass[:7],0,127,'B','F')
        coloumn=seat_range(boarding_pass[7:],0,7,'R','L')
        seat_id=(row*8)+coloumn
        seat_ids.append(seat_id)
    max_sets_ids=max(seat_ids)
    min_sets_ids=min(seat_ids)+1
    seats=set(list(range(min_sets_ids,max_sets_ids)))
    seat_ids=set(seat_ids)
    missing_seat=seats-seat_ids
    print(missing_seat)