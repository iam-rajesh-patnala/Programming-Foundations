str_num_list = input().split(",")  # spliting the input by using comma separation
repitations = int(input())  # reading no of repitations
int_num_list = list(map(int, str_num_list))  # converting string elements ti intigers in the list

length_of_int_list = len(int_num_list)  # calculating length of the list

final_repitations = repitations % length_of_int_list  # it will calculate the no of repitations

first_part = int_num_list[:final_repitations]  # seperating first elements
last_part = int_num_list[final_repitations:]  # remaing elements in the list

last_part.extend(first_part)  # extend the first_part to last_part

print(last_part)
