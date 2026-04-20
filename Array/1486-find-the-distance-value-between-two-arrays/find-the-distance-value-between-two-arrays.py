class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        count = 0

        for num in arr1:
            left_bound_index = bisect_left(arr2,num-d)
            is_valid = (left_bound_index == len(arr2) or arr2[left_bound_index] > num + d)
            count += is_valid
        return count