num = int(input())  # 5

left_space_count = num - 1
left_space = " " * left_space_count
row_output = left_space + "A"
print(row_output)

# -----------------------------------------------
count = -1
alpha = 66
hollow_space_count = 0
for i in range(2, num + 1):
    left_space_count = num - i
    left_space = " " * left_space_count
    hollow_space_count = count + i
    count += 1
    hollow_space = " " * hollow_space_count
    alpha_order = chr(alpha)
    row_output = left_space + alpha_order + hollow_space + alpha_order
    alpha += 1
    print(row_output)

alpha = alpha - 1
for j in range(1, num - 1):
    left_space_count = j
    left_space = " " * left_space_count
    hollow_space_count -= 2
    hollow_space = " " * hollow_space_count
    alpha = alpha - 1
    alpha_order = chr(alpha)
    row_output = left_space + alpha_order + hollow_space + alpha_order
    print(row_output)

# -----------------------------------------------
left_space_count = num - 1
left_space = " " * left_space_count
row_output = left_space + "A"
print(row_output)

    #     A
    #    B B
    #   C   C
    #  D     D
    # E       E
    #  D     D
    #   C   C
    #    B B
    #     A