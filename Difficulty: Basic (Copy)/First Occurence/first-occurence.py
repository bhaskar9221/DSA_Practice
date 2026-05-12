class Solution:
    def firstOccurence(self, txt, pat):
        # Idea:
        # Slide a window of size len(pat) over txt
        # Compare substring with pattern
        # Return the index when first match is found
        
        n = len(txt)
        m = len(pat)
        
        for i in range(n - m + 1):
            if txt[i:i+m] == pat:
                return i
        
        return -1