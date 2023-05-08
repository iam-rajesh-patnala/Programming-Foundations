from datetime import datetime, timedelta

starting_date = input()
ending_date = input()

start_date = datetime.strptime(starting_date, "%b %d %Y")
end_date = datetime.strptime(ending_date, "%b %d %Y")

diff = end_date - start_date
days = diff.days

print(start_date)
for i in range(days):
    increment = timedelta(days=1)
    start_date += increment
    print(start_date)
