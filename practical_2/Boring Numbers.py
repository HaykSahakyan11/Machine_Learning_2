# Boring Numbers

a_num = int(input())
char = a_num % 10
is_boring = True

while a_num > 0:
    if char != a_num % 10:
        is_boring = False
        break
    a_num //= 10

print(is_boring)
