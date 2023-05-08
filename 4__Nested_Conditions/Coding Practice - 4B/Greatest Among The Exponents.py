A = int(input())
B = int(input())

A_power_B_is_grater_than = A ** B
B_power_A_is_grater_than = B ** A

if A_power_B_is_grater_than > B_power_A_is_grater_than:
    print(A_power_B_is_grater_than)
else:
    print(B_power_A_is_grater_than)