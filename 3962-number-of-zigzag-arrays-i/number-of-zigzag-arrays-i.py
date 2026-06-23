class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        R = r - l + 1
        
        up = [0] * R
        down = [0] * R
        
        
        for v in range(R):
            up[v] = v         
            down[v] = R - 1 - v 

        for i in range(3, n + 1):
            next_up = [0] * R
            next_down = [0] * R
            
            
            curr_sum_down = 0
            for v in range(R):
                next_up[v] = curr_sum_down % MOD
                curr_sum_down += down[v]
                
            curr_sum_up = 0
            for v in range(R - 1, -1, -1):
                next_down[v] = curr_sum_up % MOD
                curr_sum_up += up[v]
                
            up = next_up
            down = next_down
            
        return (sum(up) + sum(down)) % MOD