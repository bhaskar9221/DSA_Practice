class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1

        while i<j:
            target_sum = numbers[i] + numbers[j]

            if target_sum == target:
                return [i+1,j+1]
            elif target_sum<target:
                i+=1
            else:
                j-=1