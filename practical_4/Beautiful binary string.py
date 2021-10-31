# Beautiful binary string


def beautiful_binary_string_1(b):
    counter, i = 0, 0
    limit_i = len(b) - 2

    while i < limit_i:
        if b[i] == '0' and b[i + 1] == '1' and b[i + 2] == '0':
            counter += 1
            i += 2
        i += 1
    return counter


def beautiful_binary_string_2(b):
    return b.count('010')


if __name__ == '__main__':
    n = int(input())
    b = input()

    print(beautiful_binary_string_1(b))

    # or

    print(beautiful_binary_string_2(b))
