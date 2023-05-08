side = int(input())

if side < 3:
    print("Not Polygon")
elif side == 3:
    print("Triangle")
elif side == 4:
    print("Quadrilateral")
elif side == 5:
    print("Pentagon")
elif side > 5:
    print("Big Polygon")
