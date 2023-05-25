def check_queries(no_of_students_height, no_of_quries):
    count_list = []
    for query in no_of_quries:
        count = 0
        for i in range(len(no_of_students_height)):
            if no_of_students_height[i] >= query:
                count += 1
        count_list.append(count)

    if len(count_list) > 0:
        print(*count_list, sep="\n")


def get_no_of_quries(no_of_queries):
    quries = []
    for i in range(no_of_queries):
        quries.append(int(input()))
    return quries


def get_students_heights():
    students_height = []
    students_height.extend(list(map(int, input().split())))
    return students_height


def root():
    no_of_students, no_of_queries = map(int, input().split())
    no_of_students_height = get_students_heights()
    no_of_quries = get_no_of_quries(no_of_queries)
    check_queries(no_of_students_height, no_of_quries)


root()
