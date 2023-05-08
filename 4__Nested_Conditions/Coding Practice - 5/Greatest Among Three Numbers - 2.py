A = int(input())
B = int(input())
C = int(input())


if (A > B and A > C):
    grater = A
    print(grater)
elif (B > C and B > A):
    grater = B
    print(grater)
elif (C > A and C > B):
    grater = C
    print(grater)
    
else:
    print(A)
