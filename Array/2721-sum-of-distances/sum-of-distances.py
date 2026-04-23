class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        left_sum = defaultdict(int)
        count_left = defaultdict(int)
        right_sum = defaultdict(int)
        count_right = defaultdict(int)

        for i,num in enumerate(nums):
            result[i] += i*count_left[num] - left_sum[num]
            count_left[num] += 1
            left_sum[num] += i
        

        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            result[i] += right_sum[num] - i * count_right[num]
            count_right[num] += 1
            right_sum[num] += i

        return result