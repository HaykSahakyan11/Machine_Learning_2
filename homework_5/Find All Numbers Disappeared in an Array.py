# 448. Find All Numbers Disappeared in an Array

def find_disappeared_numbers_in_array(nums):
    length_nums = len(nums)

    all_numbers_set = set(range(1, length_nums + 1))
    orig_nums_set = set(nums)

    missing_nums_set = all_numbers_set.difference(orig_nums_set)

    return list(missing_nums_set)


print(find_disappeared_numbers_in_array([4, 3, 2, 7, 8, 2, 3, 1]))  # [1, 1]
