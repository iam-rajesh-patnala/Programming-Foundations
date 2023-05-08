num1 = int(input())
num2 = int(input())

total = 0

switch = True

for i in range(1, (num2) * 2 + 1):
    if switch:
        if i % 2 == 0:
            val = num1**i
            total += val
            switch = False
    else:
        if i % 2 == 0:
            val = (-num1**i)
            total += val
            switch = True
        
print(total)