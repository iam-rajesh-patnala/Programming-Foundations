from datetime import datetime, timedelta

date = input()

formatting_date = datetime.strptime(date, "%d %b %Y")

before = timedelta(days=-1)
after = timedelta(days=1)

print(formatting_date + before)
print(formatting_date)
print(formatting_date + after)
