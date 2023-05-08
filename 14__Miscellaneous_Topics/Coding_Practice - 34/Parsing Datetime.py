from datetime import datetime

input_date = input()

date_format = datetime.strptime(input_date, "%d %b %Y")  # type: ignore
print(date_format)
