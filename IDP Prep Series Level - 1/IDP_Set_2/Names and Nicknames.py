def root():
    no_of_people = int(input())
    for i in range(no_of_people):
        names = int(input())
        name_list = []
        condition = "No"
        for name in range(names):
            person_name_and_nick_name = input().split()
            if person_name_and_nick_name not in name_list:
                name_list.append(person_name_and_nick_name)
            else:
                condition = "Yes"
        print(condition)

root()

# -----------------------------------------------------

def check_name_and_nick_name_are_same(names, nick_names):
    are_duplicates_exist = "No"
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if(names[i] == names[j] and nick_names[i] == nick_names[j]):
                are_duplicates_exist = "Yes"
    return are_duplicates_exist
    
def read_names_and_nick_names(no_of_persons):
    names, nick_names = [], []
    for i in range(no_of_persons):
        name, nick_name = input().split()
        names.append(name)
        nick_names.append(nick_name)
    return names, nick_names
        
def main():
    test_cases = int(input())
    for i in range(test_cases):
        no_of_persons = int(input())
        names, nick_names = read_names_and_nick_names(no_of_persons)
        are_name_and_nick_name_same = check_name_and_nick_name_are_same(names, nick_names)
        print(are_name_and_nick_name_same)
        
main()