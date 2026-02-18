class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        x_backup = x

        while x>0:
            a = x%10
            reverse = reverse*10 + a
            x = x//10
        return reverse == x_backup