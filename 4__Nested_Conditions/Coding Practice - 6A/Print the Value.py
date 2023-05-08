S = input()

mul = S[-1] 

num = int(S[:-1])

total = 0

if mul == "T":
    total+= num * 10
elif mul == "H":
    total+= num * 100
elif mul == "K":
    total+= num * 1000

print(total)