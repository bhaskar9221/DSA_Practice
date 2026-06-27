class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_length = frequency[1] - (frequency[1] % 2 ^ 1)

        del frequency[1]

        for base_num in frequency:
            current_length  = 0
            current_num = base_num

            while frequency[current_num] > 1:
                current_num = current_num**2
                current_length += 2
            
            if frequency[current_num]:
                current_length += 1
            else:
                current_length -= 1
            
            max_length = max(max_length, current_length)
        return max_length