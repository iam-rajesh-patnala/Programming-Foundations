grade = float(input())

marks_grater_85 = grade > 85
marks_grater_70_less_85 = grade > 70 and grade <= 85
marks_grater_60_less_70 = grade >= 60 and grade <= 70

if marks_grater_85:
    print("A")
elif marks_grater_70_less_85:
    print("B")
elif marks_grater_60_less_70:
    print("C")
else:
    print("F")
