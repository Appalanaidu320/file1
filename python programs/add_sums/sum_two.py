nums=[3,2,4]
target = 6
flag=0
print(len(nums))
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]== target):
         flag=1
    if flag==1:
        break;
    
 
if flag==1:
     print(i, j)


