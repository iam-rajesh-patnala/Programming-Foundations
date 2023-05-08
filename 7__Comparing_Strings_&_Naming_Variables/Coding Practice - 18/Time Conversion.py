time = input()

hms =  time[-1]

actual_time =int(time[:-1])


if hms.lower() == 's':
    convert = round(actual_time/ 3600, 2)
    print(str(convert) + "H")
else:
    convert = round(actual_time / 60, 2)
    print(str(convert) + "H")
