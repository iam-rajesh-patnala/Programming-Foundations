def last_occur(seq, uniq):
    count = -1
    index = []
    for char in seq:
        if int(char) == uniq:
            count += 1
            index += [count]
        else:
            count += 1
    print(index[-1])


seq = input().split()
uniq = int(input())
last_occur(seq, uniq)
