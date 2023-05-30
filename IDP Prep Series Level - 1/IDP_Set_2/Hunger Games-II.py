def get_last_char(no_of_people, no_of_choco, random_no):
    
    initial_chair = random_no

    for i in range(1, no_of_choco):
        if initial_chair < no_of_people:
            initial_chair += 1
        else:
            initial_chair = 1
    print(initial_chair)




def root():
    test_cases = int(input())
    for i in range(test_cases):
        no_of_people, no_of_choco, random_no = map(int, input().split())
        get_last_char(no_of_people, no_of_choco, random_no)

root()


# -----------------------------------------------
def get_winning_chair_number(no_of_players, chocolates, start_position):
    current_chair_position = start_position
    chocolates -= 1
    while(chocolates != 0):
        current_chair_position += 1
        chocolates -= 1
        if(current_chair_position > no_of_players):
            current_chair_position %= no_of_players
    return current_chair_position

def main():
    t = int(input())
    for i in range(t):
        no_of_players, chocolates, start_position = map(int, input().split())
        winning_chair_number =  get_winning_chair_number(no_of_players, chocolates, start_position)
        print(winning_chair_number)
main()