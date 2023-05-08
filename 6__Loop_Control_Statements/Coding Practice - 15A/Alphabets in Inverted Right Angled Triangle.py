num = int(input())

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

for i in range(num):
    result = ""
    for j in range(num-i):
        result += alphabets[j] + " "
    print(result)