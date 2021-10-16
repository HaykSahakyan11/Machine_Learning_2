# The most divisor-rich number

def divisor(num):
    count = 0
    i = 1
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 2
    if i * i == num:
        count -= 1
    return count


def get_div_reach_num(a, b):
    div_count = 0
    div_rich_num = a
    for i in range(a, b + 1):
        curr_div_num = divisor(i)
        if curr_div_num > div_count:
            div_count = curr_div_num
            div_rich_num = i
    return div_rich_num


print(get_div_reach_num(int(input("Num 1 ")), int(input("Num 2 "))))
