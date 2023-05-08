N = int(input())

Monday = 1
Tuesday = 2
wednesday = 3
thursday = 4
Friday = 5
saturday = 6
sunday = 7

if (N == 1 or N == 2):
    print("Week Start")
elif (N == 3 or N == 4 or N == 5):
    print("Midweek")
else:
    print("Weekend")
