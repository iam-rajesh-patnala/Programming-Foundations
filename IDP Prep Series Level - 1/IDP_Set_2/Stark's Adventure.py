def get_direction(direction):
    condition = "North"
    facing = ["North", "East", "South", "West"]
    R, L = 1, -1
    for dire in direction:
        if condition != "South":
            if dire == "R":
                index = facing.index(condition) + R
                condition = facing[index % 4]
            elif dire == "L":
                index = facing.index(condition) + L
                condition = facing[index % 4]
        else:
            condition = "South"
            break
    
    if condition == "South":
        print("YES")
    else:
        print("NO")
    
def root():
    loop = int(input())
    for i in range(loop):
        direction = list(input())
        get_direction(direction)


root()

#--------------------------------------------------

def get_changed_direction(current_facing_direction, direction):
    updated_direction = None
    if (current_facing_direction == "NORTH" and direction == "R"):
        updated_direction = "EAST"
    elif (current_facing_direction == "NORTH" and direction == "L"):
        updated_direction = "WEST"
    elif (current_facing_direction == "SOUTH" and direction == "R"):
        updated_direction = "WEST"
    elif (current_facing_direction == "SOUTH" and direction == "L"):
        updated_direction = "EAST"
    elif (current_facing_direction == "EAST" and direction == "R"):
        updated_direction = "SOUTH"
    elif (current_facing_direction == "EAST" and direction == "L"):
        updated_direction = "NORTH"
    elif (current_facing_direction == "WEST" and direction == "R"):
        updated_direction = "NORTH"
    else:
        updated_direction = "SOUTH"
    return updated_direction    
    
def check_stark_saved_peter(directions):
    current_facing_direction = "NORTH"
    for each_direction in directions:
        updated_direction = get_changed_direction(current_facing_direction, each_direction)
        if(updated_direction == "SOUTH"):
            return "YES"
        current_facing_direction = updated_direction
    return "NO"

def main():
    test_cases = int(input())
    for i in range(test_cases):
        directions = input()
        is_stark_saved_peter = check_stark_saved_peter(directions)
        print(is_stark_saved_peter)
        
main()