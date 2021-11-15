from collections import Counter


def uniqueOccurrences(a_nums):
    num_conter = Counter(a_nums)
    num_values = num_conter.values()
    return len(num_values) == len(set(num_values))


nums = [int(i) for i in input().split()]
# nums = [1, 2, 2, 1, 1, 3]
print(uniqueOccurrences(nums))
