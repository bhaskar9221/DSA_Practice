#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        s = list(s)
        i,j = 0,len(s)-1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        return "".join(s)