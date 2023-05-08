first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

if (first_angle+second_angle) > third_angle and (second_angle+third_angle) >first_angle and (third_angle+first_angle) > second_angle:
    print("It's a Triangle")
else:
    print("It's not a Triangle")