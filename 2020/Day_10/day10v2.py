from collections import defaultdict
nums=[]
diff_dict={1:0,2:0,3:0}
adpadters = defaultdict(lambda:-1)

with open('input.txt') as file:

    for x in file:
        num=int(x)
        nums.append(num)
    nums.append(0)
    nums=sorted(nums)
    for index in range(len(nums)-1):
        inrange=True
        i=index+1
        while True:
            diff=nums[i]-nums[index]
            if diff>3 or i>=len(nums)-1:
                break
            adpadters[nums[index]]+=1
            i+=1

def g(d):
    count=0
    for k in d:
        val=adpadters[k]
        if val>0:
            count+=val
            for x in range(1,val+1):
                count=count+g(d[d.index(k)+x:])
        else:
            count+=val*count
        #print(val)

    return count
        

print(g(list(adpadters.keys())))
#print(adpadters.keys())