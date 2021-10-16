# Lucky Numbers

def is_lucky_num(n):
    odd, even = 0, 0
    parity = 1
    while n > 0:
        if parity:
            odd += n % 10
        else:
            even += n % 10
        parity = 1 - parity
        n //= 10
    return even == odd


def is_lucky_num_2(n):
    odd, even = 0, 0
    while n > 0:
        odd += n % 10
        n //= 10
        even += n % 10
        n //= 10
    return odd == even


a_num = int(input())
print(['No', 'Yes'][is_lucky_num(a_num)])
