num = input().split(",")
num_int = list(map(int, num))
smallest = min(num_int)
largest = max(num_int)
dif = largest - smallest
print(dif)
