s1 = input()
s2 = input()

length = len(s1)

match = False

for i in range(length):
  if s1 == s2:
    match = True
    print(i)
    break
  else:
    s1 = s1[-1] + s1[:length-1]
  
if not match:
  print("No Match")