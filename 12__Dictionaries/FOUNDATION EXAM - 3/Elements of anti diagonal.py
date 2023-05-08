num = int(input())

total_list = []

for i in range(num):
    matrix = input().split()
    matrix = list(map(int, matrix))
    total_list.append(matrix)

diagonal_nums = []
length = len(total_list)

for j in range(1, length+1):
    diagonal_nums.append(total_list[j-1][length-j]) 

print(diagonal_nums)