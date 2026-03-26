from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Not the most optimal solution...
        frequency_count = Counter(nums)
        most_commonElement = frequency_count.most_common(k)

        result = [element for element, count in most_commonElement]
        return result