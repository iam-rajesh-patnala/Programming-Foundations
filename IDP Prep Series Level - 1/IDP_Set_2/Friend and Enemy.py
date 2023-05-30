def get_enemy(persons):
    length = len(persons)
    min_num = min(persons)
    exact_person = [val for val in range(min_num, length + 1) if val not in persons]
    enemy = [i for i in range(min_num, length+1) if persons.count(i) > 1]
    print(*enemy, *exact_person)


def root():
    persons = list(map(int, input().split()))
    get_enemy(persons)


root()





"""def get_enemy_and_kidnapped_person_shirt_numbers(shirt_numbers):
    total_shirts = len(shirt_numbers)
    kidnapped_person, enemy = None, None
    
    for each_shirt_number in range(1, total_shirts + 1):
        if (shirt_numbers.count(each_shirt_number) == 2):
            enemy = each_shirt_number
            
        if (shirt_numbers.count(each_shirt_number) == 0):
            kidnapped_person = each_shirt_number
        
    return enemy, kidnapped_person

def main():
    shirt_numbers = list(map(int, input().split()))
    
    enemy, kidnapped_person = get_enemy_and_kidnapped_person_shirt_numbers(shirt_numbers)
    enemy, kidnapped_person = str(enemy), str(kidnapped_person)
    print(enemy + " " + kidnapped_person)
    
main()"""