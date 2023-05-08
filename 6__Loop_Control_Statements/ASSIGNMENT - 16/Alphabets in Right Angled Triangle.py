# num = int(input())


# if num <= 26:
#     alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
#     for i in range(1, num + 1):
#         left_space = "  " * (num - i)
#         result = ' '.join(alphabets[j] for j in range(i))
#         print(f'{left_space}{result}')




def function(num):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for i in range(1, num + 1):
        left_space = "  " * (num - i)
        result = ' '.join(alphabets[j] for j in range(i))
        print(f'{left_space}{result}')

function(num = int(input()))