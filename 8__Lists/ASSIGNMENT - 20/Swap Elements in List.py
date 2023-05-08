L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

#Write your code here

index_1 = int(input()) 
index_2 = int(input())

first = L[index_1] 
second = L[index_2]

L[index_1] = second
L[index_2] = first

print(L)