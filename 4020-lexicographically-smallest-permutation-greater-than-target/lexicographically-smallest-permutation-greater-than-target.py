class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        prefix_counts = Counter()
        match_len = 0
        for char in target:
            if prefix_counts[char] < s_counts[char]:
                prefix_counts[char] += 1
                match_len += 1
            else:
                break
        
        for i in range(match_len, -1, -1):
            if i < match_len:
                prefix_counts[target[i]] -= 1
                
            rem_counts = s_counts - prefix_counts
            
            if i == n:
                continue 
            
            target_char = target[i]
            chosen_char = None
            for c in sorted(rem_counts.keys()):
                if c > target_char and rem_counts[c] > 0:
                    chosen_char = c
                    break
            
            if chosen_char:
                rem_counts[chosen_char] -= 1
                
                suffix = []
                for c in sorted(rem_counts.keys()):
                    suffix.append(c * rem_counts[c])
                
                return target[:i] + chosen_char + "".join(suffix)
                
        return ""