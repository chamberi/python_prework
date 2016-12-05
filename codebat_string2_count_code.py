def count_code(str):
  count = 0
  for i in range(len(str) - 3):
    j = i + 1
    l = i + 3
    if str[i] == 'c' and str[j] == 'o' and str[l] \
     == 'e':
       count += 1
  return count
