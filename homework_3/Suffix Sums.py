# Suffix Sums


def suffix_sums(list_of_num: list) -> list:
    sum_list = sum(list_of_num)
    output = [sum_list]
    for elem in list_of_num[:-1]:
        output.append(output[:-2:-1][0] - elem)
    return output


a_list = list(map(float, input().split()))
print(*suffix_sums(a_list))
