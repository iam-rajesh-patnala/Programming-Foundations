def get_scores(marks, no_of_students):
    result = []
    for h in range(no_of_students):
        initial_marks = marks[h]
        count = 0
        for num in marks[h:]:
            if initial_marks > num:
                count += 1
        result.append(count)

    print(*result)
def root():
    no_of_students = int(input())
    marks = list(map(int, input().split()))
    get_scores(marks, no_of_students)

root()