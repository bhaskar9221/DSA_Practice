class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        need = Counter("balloon")
        have = Counter(text)

        answer = float('inf')

        for char in need:
            answer = min(answer, have[char] // need[char])
        
        return answer