from datetime import datetime

A, B = input().split()
A, B = int(A), int(B)
count = 0

for year in range(A, B + 1):
    for month in range(1, 13):
        date_object = datetime(year, month, 1)
        # day = datetime.strftime(date_object,"%A")
        day = date_object.strftime("%A")
        if day == "Monday":
            count += 1
print(count)
