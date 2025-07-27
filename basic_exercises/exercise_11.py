def main(num):
    ans=""
    while num:
        rem=num%10
        ans+=f"{rem} "
        num=num//10
    return ans

print(main(7536))