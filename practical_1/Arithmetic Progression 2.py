# Arithmetic Progression 2
n = int(input())
An = int(input())
m = int(input())
Am = int(input())
k = int(input())

d = (Am - An) / (m - n)
print(An + (k - n) * d)
