class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        result = [i for i, num in enumerate(nums) if num == target]
        return result