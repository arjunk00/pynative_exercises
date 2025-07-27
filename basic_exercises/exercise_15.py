def main(base, exp):
    res=base
    for i in range(exp-1):
        res=res*base
    return res

print(main(5,4))