def get_final_result(total_point_of_Amanda, total_point_of_Mary_Kom, base_prize_money):
    if total_point_of_Amanda > total_point_of_Mary_Kom:
        winner =  60 * base_prize_money
        return winner
    elif total_point_of_Mary_Kom > total_point_of_Amanda:
        looser = 40 * base_prize_money
        return looser
    else:
        winner = 45 * base_prize_money
        return winner
def get_winner(winning_result, prize_money, base_prize_money):
    total_point_of_Amanda = 0
    total_point_of_Mary_Kom = 0
    for result in winning_result:
        if result == "A":
            total_point_of_Amanda += 2
        elif result == "M":
            total_point_of_Mary_Kom += 2
        elif result == "D":
            total_point_of_Mary_Kom += 1
            total_point_of_Amanda += 1

    op = get_final_result(total_point_of_Amanda, total_point_of_Mary_Kom, base_prize_money)
    print(prize_money - op)


def root():
    no_of_matches = int(input())
    for i in range(no_of_matches):
        base_prize_money = int(input())
        prize_money = 100 * base_prize_money
        winning_result = input().upper()

        get_winner(winning_result, prize_money, base_prize_money)

root()

# ---------------------------------

def get_marykom_prize_money(match_results, prize_money):
    no_of_marykom_wins = match_results.count("M")
    no_of_amanda_wins = match_results.count("A")
    
    marykom_prize_money = None
    if (no_of_marykom_wins > no_of_amanda_wins):
        marykom_prize_money = prize_money * (60/100)
    elif (no_of_marykom_wins < no_of_amanda_wins):
        marykom_prize_money = prize_money * (40/100)
    elif (no_of_marykom_wins == no_of_amanda_wins):
        marykom_prize_money = prize_money * (55/100)
    return marykom_prize_money

def main():
    t = int(input())
    for i in range(t):
        prize_money = int(input()) * 100
        match_results = input()
        marykom_prize_money = get_marykom_prize_money(match_results, prize_money)
        print(int(marykom_prize_money))
        
main()