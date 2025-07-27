def main(word, n):
    size=len(word)
    if n<size:
        ans=word[n:size]
        return ans
    else:
        return "error"
    
print(main("pynative", 2))