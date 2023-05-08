amount = int(input())

note_100 = 0
note_50 = 0
note_20 = 0
note_10 = 0

if amount >= 100:
    note_100 = int(amount / 100)
    amount = amount % 100
if amount >= 50:
    note_50 = int(amount / 50)
    amount = amount % 50
if amount >= 20:
    note_20 = int(amount / 20)
    amount = amount % 20
if amount == 10:
    note_10 = int(amount / 10)
    amount = amount % 10

print("100 Notes: " + str(note_100))
print("50 Notes: " + str(note_50))
print("20 Notes: " + str(note_20))
print("10 Notes: " + str(note_10))
