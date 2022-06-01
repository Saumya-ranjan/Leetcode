def func(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]  + arr[j] == target):
                print(arr.index(arr[i]),arr.index(arr[j]))
    


func([3,2,10,11,7,15],14)