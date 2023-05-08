def trace_char_freq(word):
  conv_set = set(word)
  conv_set.discard(" ")
  sorted_order = sorted(conv_set)
  print(sorted_order)
  for i in sorted_order:
    result = "{i}: {count}"
    count = word.count(i)
    result = result.format(i = i, count =count)
    print(result)





word = input()
word = word.lower()
trace_char_freq(word)