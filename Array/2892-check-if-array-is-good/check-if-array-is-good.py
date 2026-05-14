class Solution:
    def isGood(self, nums: List[int]) -> bool:
        frequency_counter = Counter(nums)
        n = len(nums) - 1
      
        has_n_twice = frequency_counter[n] == 2
        has_all_numbers = all(frequency_counter[i] == 1 for i in range(1, n))
      
        return has_n_twice and has_all_numbers