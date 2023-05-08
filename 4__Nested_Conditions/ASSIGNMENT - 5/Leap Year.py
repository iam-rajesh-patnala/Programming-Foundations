Y = int(input())

leap_year = (Y % 400) == 0
leap_year = leap_year or (((Y % 4) == 0) and ((Y % 100) != 0))


if leap_year:
    print("True")
else:
    print("False")
