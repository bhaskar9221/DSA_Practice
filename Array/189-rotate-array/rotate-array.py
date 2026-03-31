class Solution:
    def rotate(self, s: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(s)
        k %= n
        def reverse(l:int,r:int) -> None:
            while l<r:
                s[l],s[r] = s[r], s[l]
                l += 1
                r -= 1

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1) 