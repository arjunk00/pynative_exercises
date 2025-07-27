def main(num):
    orig=num
    reversed = 0
    while num:
        rem=num%10
        reversed = (reversed*10) + rem
        num=num//10
    return reversed==orig

print(main(1212))