# Largest Power of 3
n = int(input())

largest_power_of_3 = 1
n //= 3

while largest_power_of_3 <= n:
    largest_power_of_3 *= 3

print(largest_power_of_3)