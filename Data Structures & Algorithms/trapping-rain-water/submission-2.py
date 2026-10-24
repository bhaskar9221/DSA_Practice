class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)
        l = 0
        r = n-1
        leftmax, rightmax = height[l], height[r]
        result = 0

        while l<r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax,height[l])
                result += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax,height[r])
                result += rightmax-height[r]
        return result