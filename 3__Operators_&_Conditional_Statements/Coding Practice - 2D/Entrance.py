num_1 = int(input())
num_2 = input()

if (
    (num_1 > 12 and num_1 < 60)
    and (num_2 == "no")
    or (num_1 >= 60 and num_2 == "yes")
    or (num_1 <= 12 and num_2 == "yes")
):
    print(True)
else:
    print(False)
