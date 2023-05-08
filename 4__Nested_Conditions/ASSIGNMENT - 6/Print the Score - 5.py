distance = int(input())

bonus = 100

first_50 = distance * 3 + bonus
second_50 = 50 * 3 + (distance - 50) * 5 + bonus
next_100 = 50 * 3 + 50 * 5 + (distance - 100) * 6 + bonus
above_200 = 50 * 3 + 50 * 5 + 100 * 6 + (distance - 200) * 10 + bonus

if distance <= 50:
    print(first_50)
elif 51 <= distance <= 100:
    print(second_50)
elif 101 <= distance <= 200:
    print(next_100)
elif distance > 200:
    print(above_200)
