class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=b=0

        for move in moves:
            if move == 'U': a +=1
            elif move == 'D': a -= 1
            elif move == 'R' : b += 1
            elif move == 'L' : b -= 1
        return a==0 and b==0