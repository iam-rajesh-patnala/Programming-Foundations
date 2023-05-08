# list_a = input().split(",")
# list_b = input().split(",")

# len_of_list_a = len(list_a)


# for i in range(len_of_list_a):
#     n = len_of_list_a - 1 -i #negative indexing
#     num_1 = list_a[i]
#     num_2 = list_b[n]
#     result = str(num_1) + " " + str(num_2)
#     print(result)

list_a = input().split(",")
list_b = input().split(",")
length = len(list_a)

n = length - 1

for i in range(length):
    num_1 = list_a[i]
    num_2 = list_b[n - i]  # positive indexing
    result = str(num_1) + " " + str(num_2)
    print(result)
