class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = Counter(nums)

        for x in maps:
            if maps[x] == 1:
                return x