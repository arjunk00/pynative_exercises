def main(num):
    for i in range(1,num+1):
        for j in range(num+1, i, -1):
            print(i, end=" ")
        print("\n")

main(5)