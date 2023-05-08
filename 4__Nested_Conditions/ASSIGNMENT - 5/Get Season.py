month = int(input())

if month == 1 or month == 11 or month == 12:
    print("Winter")
elif month >= 2 and month <= 3:
    print("Spring")
elif month >= 4 and month <= 6:
    print("Summer")
elif month >= 7 and month <= 9:
    print("Rainy")
elif month >= 10 and month <= 11:
    print("Autumn")
