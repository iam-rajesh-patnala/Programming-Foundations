def number_of_cars_needed(no_of_people):
    no_of_cars = no_of_people // 5
    remaining_people = no_of_people % 5
    if remaining_people > 0:
        no_of_cars += 1
    print(no_of_cars)


no_of_people = int(input())
number_of_cars_needed(no_of_people)
