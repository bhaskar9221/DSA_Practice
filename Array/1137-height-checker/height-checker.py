class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0]*101

        for height in heights:
            count[height] += 1

        expected_array = []
        for height in range(1,101):
            c = count[height]
            for _ in range(c):
                expected_array.append(height)
        
        
        
        counts = 0

        for i in range(len(heights)):
            if heights[i] != expected_array[i]:
                counts += 1
        return counts