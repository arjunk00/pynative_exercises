def main(list1, list2):
    res=[]
    for i in list1:
        if i%2!=0:
            res.append(i)
    for i in list2:
        if i%2==0:
            res.append(i)
    return res

print(main([10, 20, 25, 30, 35],[40, 45, 60, 75, 90]))