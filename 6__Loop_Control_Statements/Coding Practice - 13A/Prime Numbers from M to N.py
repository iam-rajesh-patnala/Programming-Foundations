num1 = int(input())
num2 = int(input())

no_primes = True

for i in range(num1, num2+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
            no_primes = False
            
if no_primes:  
    print("No Prime Numbers Found")