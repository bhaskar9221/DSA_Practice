class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_left = 0
        count_right = 0
        count_ = 0

        for move in moves:
            if move == "L":
                count_left += 1
            elif move == "R":
                count_right += 1
            elif move == "_":
                count_ += 1
        

        return max(abs(count_left-count_right+count_),abs(count_left-count_right-count_))