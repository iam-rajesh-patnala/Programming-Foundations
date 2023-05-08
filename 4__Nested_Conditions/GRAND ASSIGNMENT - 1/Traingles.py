input1 = int(input())
input2 = int(input())
input3 = int(input())

if input1 == input2 == input3:
    print("Equilateral")
elif (input1 == input2) or (input1 == input3) or (input3 == input2):
    print("Isosceles")
else:
    print("Scalene")
