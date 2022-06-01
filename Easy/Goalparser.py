def func(x):
    hash = {"G":"G","()":"o","(al)":"al"}
    for i in hash.keys():
        if i in x:
            x = x.replace(i,hash[i])
    print(x)

func("G()(al)")