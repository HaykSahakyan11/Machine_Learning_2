# Digit Sum 2

num = int(input())
print(num % 10 + num // 10 % 10 + num // 100)