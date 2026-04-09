class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        for i,num in enumerate(nums):
            if num == target:
                index = i
                return i
        return -1