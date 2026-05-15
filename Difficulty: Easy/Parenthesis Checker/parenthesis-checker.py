class Solution:
    
    # Function to check if brackets are balanced or not.
    def isBalanced(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            # Opening brackets
            if ch in "({[":
                stack.append(ch)
            else:
                # If stack is empty or top doesn't match
                if not stack or stack.pop() != pairs[ch]:
                    return False
        
        # Stack should be empty for balanced brackets
        return len(stack) == 0