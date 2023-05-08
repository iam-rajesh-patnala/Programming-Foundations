# -----------------error is found in this code (22ee65)------------------


# def validate_atm_pin_code(pin):
#     four_digits = 4
#     six_digits = 6
#     length_pin = len(pin)
#     for digit in pin:
#         if digit.isdigit():
#             if length_pin == four_digits or length_pin == six_digits:
#                 print("Valid PIN Code")
#                 break
#             else:
#                 print("Invalid PIN Code")
#                 break
#         else:
#             print("Invalid PIN Code")
#             break


# pin = input()
# validate_atm_pin_code(pin)


# ----------------------perfect code ----------------------
def validate_atm_pin_code(pin):
    length_pin = len(pin)
    success = length_pin == 4 or length_pin == 6
    digits = True
    for char in pin:
        if not char.isdigit():
            digits = False
            break
    if success and digits:
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")


pin = input()
validate_atm_pin_code(pin)
