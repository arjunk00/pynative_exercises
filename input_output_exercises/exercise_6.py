def main(line_no):
    ans=[]
    with open("test.txt" ,"r") as f:
        text = f.readlines()
        for line in range(len(text)):
            if line !=line_no-1:
                ans.append(text[line])
    
    with open("ans.txt","w") as ansf:
        ansf.writelines(ans)

main(5)