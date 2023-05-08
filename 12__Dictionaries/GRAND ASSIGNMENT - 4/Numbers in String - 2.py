sentence = input().split()

total = 0
count = 0
condition = True
var = ""

for sub in sentence:
    length = len(sub)
    nums = ""
    if sub.isdigit():
        sub = int(sub)
        total += sub
        count+= 1
        condition = False
        
    elif condition:
        for i in range(length-1):
            if sub[i].isdigit() and sub[i+1].isdigit():
                for num in sub:
                    if num.isdigit():
                        nums+= num
                var = nums
                if len(var) > 0:
                    var = int(var)
                    total += var
                    count+= 1
                break
        else:
            for number in sub:
                if number.isdigit():
                    total+= int(number)
                    count += 1
print(total)
print(round(total/count, 2))























