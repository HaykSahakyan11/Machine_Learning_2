# Largest Number
b_num = int(input())

last_num = b_num % 10
output = False
while b_num > 0:
    if b_num % 10 < last_num:
        output = True
        break
    b_num //= 10

print(output)





# a_num_str = input()
# len_of_str_num = len(a_num_str)
# first_num = int(a_num_str[0])
# i = 1
# output = False
#
# while len_of_str_num > i:
#     if int(a_num_str[i]) > first_num:
#         output = True
#         break
#     first_num = int(a_num_str[i])
#     i += 1
#
# print(output)
