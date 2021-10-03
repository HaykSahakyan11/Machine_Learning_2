# Swap
a = input()
b = input()
print("Initial value of variable a:", a)
print("Initial value of variable b:", b)
# Your code starts here
a, b = b, a

# Your code ends here
print("Swapped value of variable a:", a)
print("Swapped value of variable b:", b)

# version_2 without using external memory

k = int(input())
n = int(input())
print("Initial value of variable a:", k)
print("Initial value of variable b:", n)
k = k + n
n = k - n
k = k - n
print("Initial value of variable a:", k)
print("Initial value of variable b:", n)
