num_range= int(input())
zero_index = []
one_index = []

for i in range(num_range):
  seq_input = input().split()
  one = seq_input[0]
  one = int(one)
  two = seq_input[1]
  two = int(two)
  zero_index.append(one)
  one_index.append(two)


zero_tuple = (max(zero_index), min(zero_index))
one_tuple = (max(one_index), min(one_index))

print(zero_tuple)
print(one_tuple)