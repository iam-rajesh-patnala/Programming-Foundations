word = input()
word = word.replace(" ", "")
word = word.replace("'", "")
word = word.lower()
r = word.split()
s = "".join(r)
if s == s[::-1]:
    print("True")
else:
    print("False")
