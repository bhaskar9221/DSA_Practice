class Solution:
    def leftRightDifference(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr

        right_sum = sum(arr)
        left_sum = 0
        
        for i in range(n):
            current_val = arr[i]
            
            right_sum -= current_val
            
            arr[i] = abs(right_sum - left_sum)
            
            left_sum += current_val
            
        return arr