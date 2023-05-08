def compare(team_a_points, team_b_points):
    if team_a_points > team_b_points:
        return "Win"
    elif team_a_points == team_b_points:
        return "Draw"
    else:
        return "Lose"
    # complete this function
    

team_a_points = int(input())         # 10
team_b_points = int(input())         # 6

compare_result = compare(team_a_points, team_b_points)# Call the compare function

print(compare_result)                  # Win
