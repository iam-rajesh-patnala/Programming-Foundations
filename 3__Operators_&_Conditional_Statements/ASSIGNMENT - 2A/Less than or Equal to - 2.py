A = int(input())
B = int(input())


if A == B:
    print("A <= B is True")
    print("B <= A is True")
elif A <= B:
    print("A <= B is True")
    print("B <= A is False")
elif B <= A:
    print("A <= B is False")
    print("B <= A is True")
