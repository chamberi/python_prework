def sum13(nums):
  counter = nums.count(13)
  countIt = 0
  delCount = 0
  newCount = 0
  initCount = sum(nums)
  for i in range(len(nums)):
    countIt += nums[i]
    if nums[i] == 13 and i != len(nums)-1 and nums[i + 1] != 13:
      delCount += nums[i + 1]
  newCount = initCount - delCount - (counter * 13)
  return newCount
