def func(nums):
    
    list = []
    for i in nums:
        count = 0
        for j in nums:
            if i>j:
                count+=1
        list.append(count)
    print(list)
        
func([8,1,2,2,3])

# BruteForce Method