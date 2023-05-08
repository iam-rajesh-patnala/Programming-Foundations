N = int(input())

notes_5 = int(N / 5)

rem_notes = 0


if (N % 5 != 0):
    print("5:" + str(notes_5))
    rem_notes = N % 5
    print("1:" + str(rem_notes))

else:
    print("5:" + str(notes_5) )
    rem_notes = N % 5
    print("1:" + str(rem_notes))
