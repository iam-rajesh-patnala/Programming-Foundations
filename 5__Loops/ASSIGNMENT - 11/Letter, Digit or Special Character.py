word = input()[:7:2]


if word.isdigit():
    print("Digit")
elif word.isupper():
    print("Uppercase Letter")
elif word.islower():
    print("Lowercase Letter")
else:
    print("Special Character")
