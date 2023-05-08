def get_discount(amount):
    if amount < 500:
        discount_value = amount * 0.05
        amount -= discount_value
        print(amount)
    elif amount >= 500 and amount < 2500:
        discount_value = amount * 0.1
        amount -= discount_value
        print(amount)
    else:
        discount_value = amount * 0.2
        amount -= discount_value
        print(amount)


amount = int(input())
get_discount(amount)
