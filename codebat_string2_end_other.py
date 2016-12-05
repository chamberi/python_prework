def end_other(a, b):
  aLow = a.lower()
  bLow = b.lower()
  if aLow.endswith(bLow) or bLow.endswith(aLow):
    return True
  else:
    return False
