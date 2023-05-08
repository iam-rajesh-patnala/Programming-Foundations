num1 = int(input())
num2 = int(input())


is_divisible = []

div = 1

for i in range(num1, num2+1):
    if i % 3 == 0:
        div*= i

#         is_divisible.append(i)



# for num in is_divisible:
#     div *= num

print(div)

