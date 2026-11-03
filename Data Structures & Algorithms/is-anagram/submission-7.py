from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ta = Counter(s)
        Tb = Counter(t)

        return Ta == Tb