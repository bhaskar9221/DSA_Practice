class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n

        positive_index = 0
        negative_index = 1

        for i in range(n):
            if nums[i] < 0:
                result[negative_index] = nums[i]
                negative_index += 2
            else:
                result[positive_index] = nums[i]
                positive_index += 2
        return result