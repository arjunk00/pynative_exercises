def reverse(num):
    reversed=0
    while num:
        rem=num%10
        reversed=(reversed*10)+rem
        num=num//10
    return reversed

print(1234321==reverse(123431))