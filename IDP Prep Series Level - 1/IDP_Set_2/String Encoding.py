def check_diff(first_seq, last_seq):
    diff = (ord(first_seq[0]) - ord(last_seq[0])) % 26
    condition = "Yes"
    for i in range(len(first_seq)):
        if (ord(first_seq[i]) - ord(last_seq[i])) % 26 != diff:
            condition = "No"
            break
    return condition




def root():
    first_seq, last_seq = input(), input()
    print(check_diff(first_seq, last_seq))
root()