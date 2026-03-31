class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left,right = 0,len(height)-1
        leftmax,rightmax = height[left], height[right]

        while left<right:
            if leftmax<rightmax:
                left += 1
                leftmax = max(leftmax,height[left])
                result += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax,height[right])
                result += rightmax - height[right]
        return result 