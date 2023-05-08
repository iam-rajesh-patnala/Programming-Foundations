N = int(input())

group_A = [1, 3, 5, 7,9]
group_B = [2, 4, 6, 8, 10]

rem = N % 2

if (rem in group_A):
    print("Group A")
else:
    print("Group B")