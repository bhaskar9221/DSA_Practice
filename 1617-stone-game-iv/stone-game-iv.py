class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        Determine if Alice wins the square game with optimal play.
      
        Game rules: Players take turns removing a perfect square number of stones.
        The player who removes the last stone wins.
      
        Args:
            n: Number of stones initially in the pile
          
        Returns:
            True if Alice (first player) wins, False otherwise
        """
        from functools import cache
      
        @cache
        def can_win(remaining_stones: int) -> bool:
            
            
            if remaining_stones == 0:
                return False
          
            square_root = 1
            while square_root * square_root <= remaining_stones:
                stones_to_remove = square_root * square_root
              
                if not can_win(remaining_stones - stones_to_remove):
                    return True
                  
                square_root += 1
          
            return False
      
        return can_win(n)