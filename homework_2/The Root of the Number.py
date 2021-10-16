# The Root of the Number
n = int(input())
root = 0

print(n)
while n:
    root += n % 10
    n //= 10
    if not n and root >= 10:
        n, root = root, n
        print(n)
print(root)
