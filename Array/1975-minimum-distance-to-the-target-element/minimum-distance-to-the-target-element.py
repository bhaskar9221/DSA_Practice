class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_abs = float('inf')
        for i  in range(len(nums)):
            
            if nums[i] == target:
                min_abs = min(min_abs,abs(i-start))
        return min_abs