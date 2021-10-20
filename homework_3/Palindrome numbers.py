# Palindrome numbers

def is_palindrome_num(num: int) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    return False


def palindrome_numbers(a: int, b: int) -> list:
    output = [i for i in range(a, b + 1) if is_palindrome_num(i)]
    return output


num_1 = int(input("Num1 "))
num_2 = int(input("Num2 "))
print(*palindrome_numbers(a=num_1, b=num_2))
