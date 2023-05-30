def get_product(number):
    if (len(number) == 0):
        return 0
    product = 1
    for each_num in number:
        product *= each_num
    return product
def root():
    number = int(input())
    digits = list(map(int, str(number)))
    result = get_product(digits)
    print(result)

root()