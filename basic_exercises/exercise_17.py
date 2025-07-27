def main(num):
    num1=0
    num2=1
    for i in range(num):
        print(num1)
        result = num1+num2
        num1=num2
        num2=result

main(15)