class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        def palindrome(i,j) -> bool:
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        while i<j:
            if s[i] != s[j]:
                return palindrome(i+1,j) or palindrome(i,j-1)
            i += 1
            j -= 1
        return True