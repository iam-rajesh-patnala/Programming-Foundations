def get_weather_report(temperature):
    if temperature < 22:
        print("Cold")
    elif temperature >= 22 and temperature < 35:
        print("Warm")
    else:
        print("Hot")


temperature = int(input())
get_weather_report(temperature)
