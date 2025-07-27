from math import sqrt
def isprime(i):
    if i<2:
        return False
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            return False
    return True
        
def main(num):
    res=[]
    for i in range(num+1):
        if isprime(i):
            res.append(i)
    return res

print(main(20)[::2])