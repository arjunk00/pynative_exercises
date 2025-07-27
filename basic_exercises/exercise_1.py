def main(x:int, y:int):
    if x*y<=1000:
        return x*y
    else:
        return x+y

res=main(200,31)
print(res)