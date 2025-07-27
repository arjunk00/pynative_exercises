import time
def main(secs):
    for i in range(secs, 0, -1):
        print(i)
        time.sleep(1)

main(5)
