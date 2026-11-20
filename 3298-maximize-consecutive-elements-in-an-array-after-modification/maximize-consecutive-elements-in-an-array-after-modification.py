class Solution:
  def maxSelectedElements(self, nums: list[int]) -> int:
    ans = 1
    prev = -math.inf
    dp0 = 1
    dp1 = 1

    for num in sorted(nums):
      if num == prev:
        dp1 = dp0 + 1  
      elif num == prev + 1:
        dp0 += 1  
        dp1 += 1  
      elif num == prev + 2:
        dp0 = dp1 + 1  
        dp1 = 1        
      else:
        dp0 = 1  
        dp1 = 1  
      ans = max(ans, dp0, dp1)
      prev = num

    return ans