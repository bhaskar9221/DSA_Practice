class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_count = Counter()

        max_length = 0
        left = 0

        for right, character in enumerate(s):
            character_count[character] += 1
        
            while character_count[character] > 1:
                character_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
    
        return max_length