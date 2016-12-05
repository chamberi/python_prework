def has22(nums):
  if len(nums) > 1:
    flag = False
    for i in range(len(nums)):
      if i == len(nums) - 1:
        return False
      j = i + 1
      if nums[i] == 2 and nums[j] == 2:
          return True
  else:
    return False
