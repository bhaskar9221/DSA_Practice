class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i,j = 0,len(nums)-1

        while i<=j:
            mid = (i+j)>>1

            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[j]:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            
            elif nums[mid] < nums[j]:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                j -= 1

        return False