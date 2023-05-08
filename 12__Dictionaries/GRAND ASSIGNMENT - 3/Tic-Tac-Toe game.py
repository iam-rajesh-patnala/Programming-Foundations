def function(matrix):
    if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O":
        print("Abhinav Wins")

    elif matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X":
        print("Anjali Wins")

    elif matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O":
        print("Abhinav Wins")

    elif matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X":
        print("Anjali Wins")

    elif matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O":
        print("Abhinav Wins")

    elif matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X":
        print("Anjali Wins")

    elif matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X":
        print("Anjali Wins")

    elif matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O":
        print("Abhinav Wins")

    elif matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X":
        print("Anjali Wins")

    elif matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O":
        print("Abhinav Wins")

    elif matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X":
        print("Anjali Wins")

    elif matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O":
        print("Abhinav Wins")

    elif matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X":
        print("Anjali Wins")

    elif matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O":
        print("Abhinav Wins")

    elif matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X":
        print("Anjali Wins")

    elif matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O":
        print("Abhinav Wins")
    else:
        print("Tie")


matrix = []

for i in range(3):
    row = input().split()
    matrix.append(row)

function(matrix)
