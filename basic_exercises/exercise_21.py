def main(val):
    for i in val:
        if '0'<=i<='9':
            return True
    return False

print(main("hell0"))