from copy import deepcopy


def rotate90_clockwise(mat):
    return [list(reversed(col)) for col in zip(*mat)]


def rotate(mat, _angle):
    _angle = _angle % 360 // 90
    for j in range(_angle):
        mat = rotate90_clockwise(mat)
    return mat


def update(mat, rotate_list, _args):
    i, j, value = map(int, _args)
    mat[i][j] = str(value)
    mat = rotate(mat, sum(rotate_list))
    return mat


def quary(mat, _args):
    i, j = map(int, _args)
    print(mat[i][j])


num = int(input())

matrix = []

for i in range(num):
    matrix.append(list(input().split()))

root = ""

rotation_list = []

first_matrix = deepcopy(matrix)

while root != "-1":
    root, *args = input().split()
    if root == "R":
        angle = int(args[0])
        rotation_list.append(angle)
        matrix = rotate(matrix, angle)
    elif root == "U":
        matrix = update(deepcopy(first_matrix), rotation_list, args)

    elif root == "Q":
        quary(matrix, args)
