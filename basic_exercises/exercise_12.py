def main(amt):
    factors=amt//10000
    rem=amt%10000
    taxable_0=1
    taxable_10=1
    taxable_factors=factors-taxable_0-taxable_10
    total_tax=((taxable_factors*10000)+rem)*0.2 + (10000*0.1)
    return total_tax

print(main(45000))