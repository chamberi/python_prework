def centered_average(nums):
  small = min(nums)
  big = max(nums)
  total = sum(nums) - small - big
  divisor = len(nums) - 2
  average = total / divisor
  return average
