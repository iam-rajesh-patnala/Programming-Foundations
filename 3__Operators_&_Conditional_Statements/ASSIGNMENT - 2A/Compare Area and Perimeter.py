length = int(input())
breadth = int(input())

area_of_the_rectangle = length * breadth

perimeter_of_the_rectangle = 2 * (length + breadth)


if area_of_the_rectangle <= perimeter_of_the_rectangle:
    print(True)
else:
    print(False)
