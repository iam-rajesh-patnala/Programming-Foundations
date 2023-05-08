def function(name, student_id):
    length = len(name)
    list_q = []
    for i in range(length):
        msg = "{} {}"
        key, value, = (
            name[i],
            student_id[i],
        )
        res = msg.format(key, value)
        list_q.append(res)
    return list_q


name = input().split(",")
student_id = input().split(",")

res = function(name, student_id)

for item in sorted(res):
    print(item)
