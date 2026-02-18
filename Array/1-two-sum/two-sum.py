class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i,num in enumerate(nums):
            difference=target-num

            if difference in table:
                return [table[difference],i]
            table[num] = i