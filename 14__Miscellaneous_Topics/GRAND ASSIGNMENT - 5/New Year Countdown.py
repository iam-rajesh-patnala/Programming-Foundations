from datetime import datetime, timedelta

date = input()
formated_given_year_date = datetime.strptime(date, "%b %d %Y %I:%M %p")
given_year = formated_given_year_date

nxt_year = formated_given_year_date.year + 1

next_year_date = "Jan 01 {}".format(nxt_year)
formated_next_year_date = datetime.strptime(next_year_date, "%b %d %Y")
next_year = formated_next_year_date


duration = (next_year - given_year).total_seconds()

hours = int(duration // 3600)
minutes = int(duration % 3600 // 60)

print("{} hours {} minutes".format(hours, minutes))


"""
#stackoverflow

from datetime import datetime

def get_duration(duration):
    hours = int(duration / 3600)
    minutes = int(duration % 3600 / 60)
    seconds = int((duration % 3600) % 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

format_str = '%Y-%m-%d %H:%M:%S'
start_date_str = '2018-07-03 16:03:00'
end_date_str = '2018-07-05 00:00:00'

start_date = datetime.strptime(start_date_str, format_str)
end_date = datetime.strptime(end_date_str, format_str)
duration = (end_date - start_date).total_seconds()

print(get_duration(duration))

"""
