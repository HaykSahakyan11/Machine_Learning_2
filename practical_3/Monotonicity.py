# Monotonicity

def is_monoton(a_list):
    is_asc = True
    is_desc = True
    for i in range(1, len(a_list)):
        if a_list[i] <= a_list[i - 1]:
            is_asc = False
        if a_list[i] >= a_list[i - 1]:
            is_desc = False

    if is_asc:
        return "Ascending"
    if is_desc:
        return "Descending"
    return "Neither"


a_list_int = list(map(int, input().split()))
print(is_monoton(a_list_int))
