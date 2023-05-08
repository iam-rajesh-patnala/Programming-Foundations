def sum_of_the_digits(number):
    total_num = 0
    for num in str(number):
        total_num += int(num)
    print(total_num)


number = int(input())
sum_of_the_digits(number)
# Call the sum_of_the_digits function
