Temp = float(input())

Freezing = int(Temp) < 0
Very_cold = 0 <= int(Temp) < 10
cold = 10 <= int(Temp) < 20
normal = 20 <= int(Temp) < 30
hot = 30 <= int(Temp) < 40
veryhot = int(Temp) >= 40

if Freezing:
    print("Freezing weather")
elif Very_cold:
    print("Very Cold weather")
elif cold:
    print("Cold weather")
elif normal:
    print("Normal")
elif hot:
    print("Hot")
elif veryhot:
    print("Very Hot")
