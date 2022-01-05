nums=[]
diff_dict={1:0,2:0,3:0}
print(diff_dict)
with open('input.txt') as file:
    for x in file:
        num=int(x)
        nums.append(num)
    nums.append(0)
    nums=sorted(nums)
    for index in range(len(nums)-1):
        diff=nums[index+1]-nums[index]
        diff_dict[diff]+=1
    diff_dict[3]+=1
print(diff_dict)