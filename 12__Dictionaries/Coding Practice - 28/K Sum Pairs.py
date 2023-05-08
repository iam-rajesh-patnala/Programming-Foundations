def find_sum_of_pairs(x, y):
    length = len(x) - 1  # calculating length
    total_set = set()  # creating empty sett
    for i in range(length):
        num_1 = x[i]  # storing 1st value
        num_2 = y - num_1  # subtract the 1st index value from pair sum
        rem_index = x[i + 1 :]
        if num_2 in rem_index:  # membership checking
            pair = (num_1, num_2)  # converting to tuple
            sorted_order = tuple(sorted(pair))  # when we sorted it will converting tuple to list
            total_set.add(sorted_order)  # adding tuple list values to set
    return total_set  # return the final output to result


str_num_list = input().split(",")
pair_sum = int(input())
# converting str list to int list
int_num_list = list(map(int, str_num_list))
result = find_sum_of_pairs(int_num_list, pair_sum)
result = sorted(result)

for j in result:
    print(j)
