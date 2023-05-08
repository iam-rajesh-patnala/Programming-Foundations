amount = int(input())

note_500 = 0
note_50 = 0
note_10 = 0
note_1 = 0

if amount >= 500:
    note_500 = int(amount / 500)
    amount = amount % 500
if amount >= 50:
    note_50 = int(amount / 50)
    amount = amount % 50
if amount >= 10:
    note_10 = int(amount / 10)
    amount = amount % 10
if amount >= 1:
    note_1 = int(amount / 1)
    amount = amount % 1

print(
    ("500: " + str(note_500) + " ")
    + ("50: " + str(note_50) + " ")
    + ("10: " + str(note_10) + " ")
    + ("1: " + str(note_1) + " ")
)
