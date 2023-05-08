first_number = int(input())
second_number = int(input())
third_number = int(input())

first_number_and_second_number = first_number - second_number
second_number_and_third_number = second_number - third_number
third_number_and_first_number = third_number - first_number

(case_1, case_2, case_3) = (
    first_number_and_second_number,
    second_number_and_third_number,
    third_number_and_first_number,
)

if case_1 < 25 and case_2 < 25 and case_3 < 25:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")
