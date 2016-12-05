def cat_dog(str):
  dog = 0
  cat = 0
  for i in range(len(str) -2 ):
    j = i + 1
    k = i + 2
    if str[i] == 'c' and str[j] == 'a' and str[k] == 't':
      cat += 1
    elif str[i] == 'd' and str[j] == 'o' and str[k] == 'g':
      dog += 1
  if dog == cat:
    return True
  else:
    return False
