loop = int(input())

extend_list = []

for i in range(loop):
    val = input().split()
    extend_list.extend(val)

extend_list.sort()

print(extend_list)
