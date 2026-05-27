class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in reversed(s):
            if c == " ":
                if count:
                    break
            else:
                count += 1
        return count