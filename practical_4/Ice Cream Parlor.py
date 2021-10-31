# Ice Cream Parlor

def whatFlavors(cost, money):
    set_cost = set(cost)
    half = money / 2
    rev_cost = cost[::-1]

    for i in range(len(cost)):
        if cost[i] != half and (money - cost[i]) in set_cost:
            return print(
                f"{i + 1}"
                f" {cost.index(money - cost[i]) + 1}"
            )
        elif cost[i] == half and \
                i != abs(rev_cost.index(cost[i]) - len(cost) + 1):
            return print(
                f"{i + 1}"
                f" {abs(rev_cost.index(cost[i]) - len(cost))}"
            )


if __name__ == '__main__':
    t = int(input('t '))

    for t_itr in range(t):
        money = int(input('money '))

        n = int(input('n '))

        cost = list(map(int, input(f'cost {t_itr}').rstrip().split()))

        whatFlavors(cost, money)