i = input()  # 25C


# if temperature is in kelvin
if i[-1] == "k" or i[-1] == "K":
    x = float(i[:-1])
    c = x - 273
    k = x
    f = (9 * c / 5) + 32
    print(str(round(float(c), 2)) + "C")
    print(str(round(float(f), 2)) + "F")
    print(str(round(float(k), 2)) + "K")


# if temperature is in celcius
if i[-1] == "c" or i[-1] == "C":
    x = float(i[:-1])
    c = x
    k = x + 273
    f = (9 * c / 5) + 32
    print(str(round(float(c), 2)) + "C")
    print(str(round(float(f), 2)) + "F")
    print(str(round(float(k), 2)) + "K")

    # 25.0C
    # 77.0F
    # 298.0K


# if temperature is in fahrenheit
if i[-1] == "f" or i[-1] == "F":
    x = float(i[:-1])
    c = (x - 32) * 5 / 9
    k = c + 273
    f = x
    print(str(round(float(c), 2)) + "C")
    print(str(round(float(f), 2)) + "F")
    print(str(round(float(k), 2)) + "K")
