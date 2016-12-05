def sum67(nums):
  tempDelCount = 0
  delCount = 0
  count = 0
  flag = False
  for i in range(len(nums)):
    count += nums[i]
    if flag == False and nums[i] == 6:
      flag = True
    if flag == True:
      tempDelCount += nums[i]
    if flag == True and nums[i] == 7:
      delCount += tempDelCount
      tempDelCount = 0
      flag = False
  newCount = count - delCount
  return newCount
