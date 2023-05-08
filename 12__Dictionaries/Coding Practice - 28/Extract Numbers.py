str_input = input().split(",")

list_final = []

for num in str_input:
    if num.isdigit():
        list_final += [int(num)]
print(list_final)
