# Digit Product
n = int(input())
dig_prod = 0
while n:
    digit = n % 10
    if digit:
        if dig_prod:
            dig_prod *= digit
        else:
            dig_prod = digit
    n //= 10
print(dig_prod)

