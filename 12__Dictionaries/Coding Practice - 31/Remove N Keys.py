alphabets = {
    "a": 97,
    "b": 98,
    "c": 99,
    "d": 100,
    "e": 101,
    "f": 102,
    "g": 103,
    "h": 104,
}

data = input().split()

for key in data:
    if key in alphabets:
        del alphabets[key]

print(alphabets)
