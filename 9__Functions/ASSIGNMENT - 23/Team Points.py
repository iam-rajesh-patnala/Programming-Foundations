def calculate_league_points(wins, draws, losses):
    total = 0
    for i in range(wins):
        total += 4
    for j in range(draws):
        total += 2
    for k in range(losses):
        total -= 1
    print(total)
    # Complete this function


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
calculate_league_points(wins, draws, losses)  # Call the calculate_league_points function
