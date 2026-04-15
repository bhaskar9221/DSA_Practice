class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        answer = float('inf')

        for i in range(n):
            if words[i] == target:

                distance = abs(i-startIndex)
                current_distance = n - distance
                answer = min(answer,min(distance,current_distance))

        return answer if answer != float('inf') else  -1