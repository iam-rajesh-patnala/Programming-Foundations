students_dict = {"Ram": "Cricket", "Naresh": "Football", "Vani": "Tennis", "Rahim": "Cricket"}

num = int(input())

for i in range(num):
    key, value = input().split()
    students_dict[key] = value
print(students_dict)
