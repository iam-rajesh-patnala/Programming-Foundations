from datetime import datetime

date = input()

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")  # type: ignore
modified = date_time.strftime("%d/%m/%Y %H:%M:%S")

print(modified)
