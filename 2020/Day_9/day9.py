with open('input.txt') as file:
    nums=[]
    for line in file:
        prev=nums[-25:]
        #print(prev)
        num=int(line)
        found=False
        for x in prev:
            for y in prev:
                num_sum=x+y
                if num_sum==num:
                    
                    found=True
        
        if not(found)and len(prev)==25:
            print(num)
            break
        nums.append(num)
                
    print(nums[:25])
