amount = int(input())

note_1000 = 0
note_500 = 0
note_100 = 0
note_50 = 0
note_20 = 0
note_5 = 0
note_1 = 0

if amount >= 1000:
    note_1000 = int(amount / 1000)
    amount = amount % 1000
if amount >= 500:
    note_500 = int(amount / 500)
    amount = amount % 500
if amount >= 100:
    note_100 = int(amount / 100)
    amount = amount % 100
if amount >= 50:
    note_50 = int(amount / 50)
    amount = amount % 50
if amount >= 20:
    note_20 = int(amount / 20)
    amount = amount % 20
if amount >= 5:
    note_5 = int(amount / 5)
    amount = amount % 5
if amount >= 1:
    note_1 = int(amount / 1)
    amount = amount % 1

print("1000:" + str(note_1000))
print("500:" + str(note_500))
print("100:" + str(note_100))
print("50:" + str(note_50))
print("20:" + str(note_20))
print("5:" + str(note_5))
print("1:" + str(note_1))
