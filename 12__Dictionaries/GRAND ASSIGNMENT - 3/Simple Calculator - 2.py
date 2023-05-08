calculate = input().split()

if calculate[1] == "+":
    num_1 = int(calculate[0])
    num_2 = int(calculate[-1])
    print(num_1 + num_2)
elif calculate[1] == "*":
    num_1 = int(calculate[0])
    num_2 = int(calculate[-1])
    print(num_1 * num_2)
elif calculate[1] == "-":
    num_1 = int(calculate[0])
    num_2 = int(calculate[-1])
    print(num_1 - num_2)
elif calculate[1] == "/":
    num_1 = int(calculate[0])
    num_2 = int(calculate[-1])
    print(num_1 / num_2)
elif calculate[1] == "%":
    num_1 = int(calculate[0])
    num_2 = int(calculate[-1])
    print(num_1 % num_2)
