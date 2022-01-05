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
            invalid=num
            break
        nums.append(num)
    print(invalid)        
    
    for x in range(len(nums)):
        for y in range(len(nums)):
            val=sum(nums[x:y])
            if val==invalid and not(x==y):
                print(x,y)
                
                print(max(nums[x:y])+min(nums[x:y]))
                #print(nums[x]+nums[y-1])
