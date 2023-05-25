# def get_single_entry(number_seq):
#     single_entry = 0
#     for num in number_seq:
#         single_entry ^= num
#     print(single_entry)

# number_seq = list(map(int, input().split()))
# get_single_entry(number_seq)


# ````````````````````````````````````````````````

def get_single_entry(number_seq):

    single_num = None
    for num in number_seq:
        if number_seq.count(num) == 1:
            single_num = num
    print(single_num)



number_seq = list(map(int, input().split()))
get_single_entry(number_seq)