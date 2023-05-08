S = input()

first_3_words = S[:3]
remaining_words = int(S[3:])

condition_1 = first_3_words == "NXT"
condition_2 = remaining_words % 2 == 0 or remaining_words % 7 == 0

if condition_1 and condition_2:
    print("Special String")
else:
    print("Not a Special String")
