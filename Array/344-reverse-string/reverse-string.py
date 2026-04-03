class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        #Using Two-Pointers Method
        i,j = 0, len(s)-1

        while i<j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1