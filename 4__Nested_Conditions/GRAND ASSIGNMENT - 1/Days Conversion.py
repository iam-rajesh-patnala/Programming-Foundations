days = int(input())
years = int(days / 365)
ream_days = days - (years) * 365
weeks = int(ream_days / 7)
days = ream_days - weeks * 7

print(str(years) + " years " + str(weeks) + " weeks " + str(days) + " days ")
