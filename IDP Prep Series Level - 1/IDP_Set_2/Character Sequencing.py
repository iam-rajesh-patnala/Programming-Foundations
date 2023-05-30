def get_alpha_list(num_list):
    new_alpha_list = ""
    alpha_list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for num in num_list:
        new_alpha_list += alpha_list[int(num) - 1]

    return new_alpha_list
def root():
    num_list = input().split()
    print(get_alpha_list(num_list))

root()


# -------------------------------------------

def get_resultant_string(numbers):
    resultant_string = ""
    for each_number in numbers:
        character_ascii_value = each_number + 96
        resultant_string += chr(character_ascii_value)
    return resultant_string
    
def main():
    numbers = list(map(int, input().split()))
    resultant_string = get_resultant_string(numbers)
    print(resultant_string)
    
main()