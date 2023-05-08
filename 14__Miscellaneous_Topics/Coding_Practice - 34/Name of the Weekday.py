from datetime import datetime

date = input()

formating = datetime.strptime(date, "%d %b %Y")

weekday = formating.strftime("%A")

print(weekday)
