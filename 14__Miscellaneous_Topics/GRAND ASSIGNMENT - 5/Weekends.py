from datetime import datetime, timedelta

date_1 = input()  # 25 Jan 2021
date_2 = input()  # 214 Feb 2021

saturday_count = 0
sunday_count = 0

date_1 = datetime.strptime(date_1, "%d %b %Y")
date_2 = datetime.strptime(date_2, "%d %b %Y")
number_of_days = (date_2 - date_1).days


for i in range(number_of_days + 1):
    delta = timedelta(days=i)
    inc = date_1 + delta

    # print(final_date, final_date.strftime("%A"))
    if inc.strftime("%A") == "Saturday":
        saturday_count += 1
    if inc.strftime("%A") == "Sunday":
        sunday_count += 1

print("Saturday: {}".format(saturday_count))
print("Sunday: {}".format(sunday_count))
