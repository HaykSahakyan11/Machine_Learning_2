# Index Sum
def index_sum(list_1, list_2):
    sum = 0
    for i in list_2:
        sum += list_1[i]
    return sum


A_list = list(map(float, input().split()))
N_list = list(map(int, input().split()))

print(index_sum(A_list, N_list))
