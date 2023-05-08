N = int(input())

if(N % 10 == 0 ):
    print("Divisible by 10")
elif(N % 5 == 0  and N % 10 != 0):
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")