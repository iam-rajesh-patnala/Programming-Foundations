# N = int(input(""))

# if N == 0:
#     print("No Output")

# if N >= 0 and N <= 100:
#     teamsData = {}
#     for i in range(N):
#         values = input().split(";")
#         first_team = values[0].strip()
#         second_team = values[1].strip()
#         match_result = values[2].strip()

#         if first_team not in teamsData:
#             teamsData[first_team] = [0, 0, 0, 0, 0]

#         if second_team not in teamsData:
#             teamsData[second_team] = [0, 0, 0, 0, 0]

#         if first_team in teamsData and second_team in teamsData:
#             teamsData[first_team][0] += 1
#             teamsData[second_team][0] += 1

#             if match_result == "win":
#                 teamsData[first_team][1] += 1
#                 teamsData[second_team][2] += 1

#             elif match_result == "loss":
#                 teamsData[first_team][2] += 1
#                 teamsData[second_team][1] += 1

#             elif match_result == "draw":
#                 teamsData[first_team][3] += 1
#                 teamsData[second_team][3] += 1

#     for t in teamsData:
#         teamsData[t][4] = teamsData[t][1] * 3 + teamsData[t][3]

# teamsData = sorted(teamsData.items(), key=lambda points: points[1][4], reverse=True)


# for t in teamsData:
#     output = (
#         f"Team: {t[0]}, Matches Played: {t[1][0]}, Won: {t[1][1]}, Lost: {t[1][2]}, Draw: {t[1][3]}, Points: {t[1][4]}"
#     )
#     print(output)


def max_square(matrix, col, row):
    res = [[0 for i in range(row + 1)] for j in range(col + 1)]
    side_length = 0
    for i in range(1, len(res)):
        for j in range(1, len(res[0])):
            if matrix[i - 1][j - 1] == "X":
                res[i][j] = min(res[i][j - 1], res[i - 1][j], res[i - 1][j - 1]) + 1
                side_length = max(side_length, res[i][j])

    return side_length * side_length


col, row = map(int, input().split())
matrix = []

for i in range(col):
    input_matrix = input().split()
    matrix.append(input_matrix)

function = max_square(matrix, col, row)

print(function)
