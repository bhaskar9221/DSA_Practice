class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)-1

        while i<=j:
            nums[i], nums[j] = nums[i]*nums[i], nums[j]*nums[j]
            
            i += 1
            j -= 1
        return sorted(nums)