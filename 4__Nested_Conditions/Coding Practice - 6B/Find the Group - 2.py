N = int(input())
# N = 24

Group_1 = [1, 7, 13, 19, 25]
Group_2 = [2, 8, 14, 20, 26]
Group_3 = [3, 9, 15, 21, 27]
Group_4 = [4, 10, 16, 22, 28]
Group_5 = [5, 11, 17, 23, 29]
Group_6 = [6, 12, 18, 24, 30]

rem = N % 6 

if (rem in Group_1):
    print("Group 1")
elif (rem in Group_2):
    print("Group 2")
elif (rem in Group_3):
    print("Group 3")
elif (rem in Group_4):
    print("Group 4")
elif (rem in Group_5):
    print("Group 5")
elif (rem in Group_6):
    print("Group 6")
else:
    print("Group6")