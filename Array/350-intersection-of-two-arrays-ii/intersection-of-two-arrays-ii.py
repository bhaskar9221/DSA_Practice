class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        counts = Counter(nums1)

        for num in nums2:
            if counts[num]>0:
                answer.append(num)
                counts[num] -= 1
        return answer