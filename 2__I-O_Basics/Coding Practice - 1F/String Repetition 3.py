userinput1 = input()
userinput2 = int(input())
length_of_word = len(userinput1)
start_index = length_of_word - 3
sliced_word = userinput1[start_index:]
message = sliced_word * userinput2
print(message)
