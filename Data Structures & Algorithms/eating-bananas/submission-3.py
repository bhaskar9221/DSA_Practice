class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        first_true_index = -1

        def feasible(eating_speed: int) -> bool:
            total_hours = sum((pile_size + eating_speed - 1) // eating_speed
                            for pile_size in piles)
            return total_hours <= h

        while l<=r:
            mid = (l+r)//2
            if feasible(mid):
                first_true_index = mid
                r = mid - 1
            else:
                l = mid + 1
        return first_true_index