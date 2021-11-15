# 1512. Number of Good Pairs


def numIdenticalPairs(nums):
    a_dict = {}
    count = 0
    for num in nums:
        if num not in a_dict:
            a_dict[num] = 0
        a_dict[num] += 1

    for _, value in a_dict.items():
        count += (value * (value - 1) // 2)

    return count


a_nums = [int(i) for i in input().split()]
# a_nums = [1, 2, 2, 1, 1, 3]
print(numIdenticalPairs(a_nums))
