class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            if num == 0:
                answer.append(0)
                continue
            
            digits = []
            while num>0:
                digits.append(num%10)
                num //= 10
            answer.extend(digits[::-1])
        return answer