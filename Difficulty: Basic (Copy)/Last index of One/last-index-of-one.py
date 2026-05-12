class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                return i
        return -1