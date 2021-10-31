# Bayan


def bayan():
    num = int(input("Number of stores "))
    stores = set()

    for i in range(num):
        store = input("Store {} ".format(i + 1))
        stores.add(store)
    output = num - len(stores)
    return output


print(bayan())


