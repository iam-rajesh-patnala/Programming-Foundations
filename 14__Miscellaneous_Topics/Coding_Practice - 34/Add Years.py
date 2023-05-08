from datetime import datetime, timedelta

date = input()
year = int(input())

formating = datetime.strptime(date, "%b %d %Y")
delta_year = timedelta(days=365 * year)

print(formating + delta_year)
