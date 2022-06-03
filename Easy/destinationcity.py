def func(path):
    if len(path)==1:
        for i in path:
            print(i[1])
    else:
        arr = []
        for i in path:
            arr.append(i[0])
        for i in path:
            if i[1] not in arr:
                print(i[1])


func([["Hello","Here"]])