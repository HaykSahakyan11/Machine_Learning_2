# Triangle
a = int(input())
b = int(input())
c = int(input())

if a < b:
    b, a = a, b
if a < c:
    c, a = a, c
if b < c:
    c, b = b, c

if a >= b + c:
    print("No Triangle")
elif a ** 2 == b ** 2 + c ** 2:
    print("Right Triangle")
elif a ** 2 > b ** 2 + c ** 2:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
