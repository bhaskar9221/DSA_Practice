class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0, len(nums)-1
        n = len(nums)
        k %= n

        def reverse_num(i:int, j:int) -> None:
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse_num(0,n-1)
        reverse_num(0,k-1)
        reverse_num(k,n-1)