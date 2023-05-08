time = int(input())

GM = time >= 4 and time < 12
GA = time >= 12 and time < 16
GE = time >= 16 and time < 20
GN = time >= 20 or time < 4

if GM:
    print("Good Morning")
elif GA:
    print("Good Afternoon")
elif GE:
    print("Good Evening")
elif GN:
    print("Good Night")
