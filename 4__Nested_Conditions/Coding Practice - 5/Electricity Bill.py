units = int(input())

if units < 50:
    bill = 2 * units
elif units < 150:
    bill = (2 * 50) + (3 * (units - 50))
elif units < 250:
    bill = (2 * 50) + (3 * 100) + (5 * (units - 150))
elif units >= 250:
    bill = (2 * 50) + (3 * 100) + (5 * 100) + (8 * (units - 250))

surcharge = 0.2
surcharge = bill * surcharge
print(bill + surcharge)
