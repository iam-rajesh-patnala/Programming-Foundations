def get_speed_status(speed):
    if speed < 60:
        print("Normal")
    elif speed >= 60 and speed < 80:
        print("Warning")
    else:
        print("Over Speed")


speed = int(input())
get_speed_status(speed)
# Call the get_speed_status function
