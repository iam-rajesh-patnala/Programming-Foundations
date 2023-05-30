def get_sum_of_nums(val, position, num_list):
    sum = 0
    dict_list = dict()
    for i in range(1, position+1):
        dict_list[i] = num_list[i-1]
        if i % val == 0:
            sum += dict_list[i]
    
    print(sum)
    



val, position = map(int, input().split())
num_list = list(map(int, (input().split())))

get_sum_of_nums(val, position, num_list)



# ---------------------------------------------------------


"""
def get_nth_number_sum(numbers, divisible_number):
    sum_of_numbers = 0
    for each_position in range(1, len(numbers) + 1):
        if(each_position % divisible_number == 0):
            sum_of_numbers += numbers[each_position - 1]
    return sum_of_numbers

def main():
    divisible_number, numbers_length = map(int, input().split())
    numbers = list(map(int, input().split()))
    nth_number_sum = get_nth_number_sum(numbers, divisible_number)
    print(nth_number_sum)

main()"""