def get_first_last(number_seq, num):
    first = number_seq[num:]
    last = number_seq[:-num]
    print(*first)
    print(*last)

number_seq = list(map(int, input().split(",")))
num = int(input())

get_first_last(number_seq, num)