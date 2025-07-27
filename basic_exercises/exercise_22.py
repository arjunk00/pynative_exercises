def main(val: str):
    ans=""
    splitted = val.split(" ")
    for word in splitted:
        ans+= f"{word.capitalize()} "

    return ans

str1 = "pynative.com is for python lovers"
print(main(str1))