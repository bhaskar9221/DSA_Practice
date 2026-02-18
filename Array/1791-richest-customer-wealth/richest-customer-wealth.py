class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0

        for i in range(len(accounts)):
            current = sum(accounts[i])
            if current > max_sum: max_sum = current
        return max_sum