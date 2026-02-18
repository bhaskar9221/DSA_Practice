#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        i,j = 0, len(s)-1
        s = list(s)
        while i<j:
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        return "".join(s)