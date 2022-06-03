def func(s):
    count = 0
    hash = {}
    for i in s:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+=1

    odd_present = False
    for i in hash.values():
        if i%2 == 0:
            count+=i
        else:
            count+=i-1
            odd_present = True
    if odd_present == True:
        count+=1
    print(count)
    
    
func("bananas")