# Number Of Divisors
num = int(input())

divisors_count, divisor = 0, 0
while divisor < (num ** 0.5):
    divisor += 1
    if num % divisor == 0:
        divisors_count += 2
if divisor * divisor == num:
    divisors_count -= 1
print(divisors_count)




