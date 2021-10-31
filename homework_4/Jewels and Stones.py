# Jewels and Stones

def count_jewels_in_stones(jewels, stones):
    j_set = set(jewels)
    count_jewels_in_collection = 0

    for stone in stones:
        if stone in j_set:
            count_jewels_in_collection += 1
    return count_jewels_in_collection


print(count_jewels_in_stones(jewels="aA", stones="aAAbbbb"))
