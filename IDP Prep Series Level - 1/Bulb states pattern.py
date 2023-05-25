


def update_bulb_status(bulb_status):
    current_bulb_status =[]
    for each_bulb in bulb_status:
        if each_bulb == 1:
            current_bulb_status.append(0)
        else:
            current_bulb_status.append(1)
    return current_bulb_status

def get_initial_bulb_status(rows_count):
    initial_bulb_status = []

    for i in range(rows_count):
        if i % 2 == 0:
            initial_bulb_status.append(1)
        else:
            initial_bulb_status.append(0)

    return initial_bulb_status

def get_final_result(bulb_status):
    for each_bulb in bulb_status:
        res = list(map(str, each_bulb))
        print(' '.join(res))



def get_bulb_status(rows_count):
    bulbs_on_off_status = []
    no_of_visits = rows_count

    initial_bulb_status = get_initial_bulb_status(rows_count)
    previous_bulb_on_of_status = initial_bulb_status
    bulbs_on_off_status.append(previous_bulb_on_of_status)

    for i in range(1, no_of_visits):
        current_bulb_on_of_status = update_bulb_status(previous_bulb_on_of_status)
        bulbs_on_off_status.append(current_bulb_on_of_status)
        previous_bulb_on_of_status = current_bulb_on_of_status

    return bulbs_on_off_status

def root():
    rows_count = int(input())
    bulb_status = get_bulb_status(rows_count)
    get_final_result(bulb_status)

root()