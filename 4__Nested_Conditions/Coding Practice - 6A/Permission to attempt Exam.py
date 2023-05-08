precentage = input()
medic = input()
RP = int(precentage[0:-1])

if RP >= 75:
    print("Allowed to write exam")
elif RP < 75 and medic == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
