# Tree

def print_tree(n):
    space = (n - 1) // 2
    star = 1

    while star <= n:
        print("{}{}{}".format(" " * space, "*" * star, " " * space))
        space -= 1
        star += 2


a_num = int(input())
print_tree(a_num)
