def get_right_ang_triangle(matrix, loop):
    total = 0
    for i in range(1, loop+1):
        total += sum(matrix[i-1][-i:])
    return (total)

def get_inv_right_ang_triangle(matrix, loop):
    total = 0
    for i in range(loop):
        total += sum(matrix[i][:loop - i])
    return (total)

def get_matrix(loop):
    matrix = []
    for i in range(loop):
        matrix.append(list(map(int, input().split())))

    inv_rat, rat = get_inv_right_ang_triangle(matrix, loop), get_right_ang_triangle(matrix, loop)

    print(inv_rat, rat, sep="\n")
def root():
    loop = int(input())
    get_matrix(loop)


root()




# ----------------------------------


def get_sum_of_lower_triangle(matrix):
    sum_of_lower_triangle = 0 
    for i in range(len(matrix)):
        sum_of_lower_triangle += sum(matrix[i][-i-1:])
    return sum_of_lower_triangle

def get_sum_of_upper_triangle(matrix):
    sum_of_upper_triangle = sum(matrix[0])
    for i in range(len(matrix)):
        sum_of_upper_triangle += sum(matrix[i][:-i])
    return sum_of_upper_triangle

def read_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    return matrix

def main():
    n = int(input())
    matrix = read_matrix(n)
    sum_of_upper_triangle = get_sum_of_upper_triangle(matrix)
    sum_of_lower_triangle = get_sum_of_lower_triangle(matrix)
    print(sum_of_upper_triangle)
    print(sum_of_lower_triangle)

main()