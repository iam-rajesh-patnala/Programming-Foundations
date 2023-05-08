students_dict = {"Ram": "Cricket", "Naresh": "Football", "Vani": "Tennis", "Rahim": "Cricket"}

word = input().split()
key, val = word[0], word[1]
students_dict[key] = val

print(students_dict)
