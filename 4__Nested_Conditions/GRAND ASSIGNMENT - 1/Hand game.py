Abhinav = input()
Anjali = input()

if (Abhinav == "Rock") and (Anjali == "Paper"):
    print("Anjali Wins")
elif (Abhinav == "Scissors") and (Anjali == "Rock"):
    print("Anjali Wins")
elif (Abhinav == "Paper") and (Anjali == "Scissors"):
    print("Anjali Wins")
elif Abhinav == Anjali:
    print("Tie")
else:
    print("Abhinav Wins")
