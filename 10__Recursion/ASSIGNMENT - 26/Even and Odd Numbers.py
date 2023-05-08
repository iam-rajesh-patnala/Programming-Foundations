def convert_to_int(num_list):
    new = []
    for num in num_list:
        # new.append(int(num))
        new += [int(num)]
    return new


def check_odd_even(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.sort()
    odd.sort()
    print(even, odd, sep="\n")


# num_list = list(map(int,input().split()))
num_list = convert_to_int(input().split())

check_odd_even(num_list)
