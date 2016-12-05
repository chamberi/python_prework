def double_char(str):
  dbl = ""
  for i in range(len(str)):
    dbl += str[i] + str[i]
  return dbl
