# 575. Distribute Candies


def distributeCandies(a_nums):
    len_a_nums = len(a_nums)
    trigger = len_a_nums // 2

    len_set_nums = len(set(a_nums))

    return [trigger, len_set_nums][trigger > len_set_nums]


def distributeCandies_2(c):
    number_types = len(set(c))
    return min(number_types, len(c) // 2)


a_nums = [int(i) for i in input().split()]
# a_nums = [1, 1, 2, 2, 3, 3]
print(distributeCandies(a_nums))

print(distributeCandies_2(a_nums))
