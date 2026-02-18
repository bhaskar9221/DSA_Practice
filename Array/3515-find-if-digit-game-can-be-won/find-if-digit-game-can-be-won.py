class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        single_digit = sum(x for x in nums if x<10)
        double_digit = sum(x for x in nums if x>9)
        
        return single_digit != double_digit
        