num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
list_input = input().split()
list_input = set(map(int, list_input))

if num_set.issuperset(list_input):
    print("Superset")
elif num_set.isdisjoint(list_input):
    print("Disjoint Set")
else:
    print("Subset")
