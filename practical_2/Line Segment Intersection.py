# Line Segment Intersection

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

if a1 > b1:
    a1, b1 = b1, a1
if a2 > b2:
    a2, b2 = b2, a2

if a1 > a2:
    a1, a2 = a2, a1
    b1, b2 = b2, b1
if b1 < a2:
    print(0)
elif b1 < b2:
    print(b1 - a2)
else:
    print(b2 - a2)
