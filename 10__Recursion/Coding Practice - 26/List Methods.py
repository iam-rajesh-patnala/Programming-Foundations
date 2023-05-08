num = int(input())
list_a = []


for i in range(num):
    op = input()
    input_val = op.split()
    if input_val[0] == "append":
        list_a.append(int(input_val[1]))
    elif input_val[0] == "insert":
        list_a.insert(int(input_val[1]), int(input_val[2]))
    elif input_val[0] == "remove":
        list_a.remove(int(input_val[1]))
    elif input_val[0] == "pop":
        list_a.pop()
    elif input_val[0] == "sort":
        list_a.sort()
    elif input_val[0] == "print":
        print(list_a)
