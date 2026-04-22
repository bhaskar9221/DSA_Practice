class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for q in queries:
            for word in dictionary:
                difference = sum(
                    char_q != char_d
                    for char_q, char_d in zip(q, word)
                )
                
                if difference <= 2:
                    result.append(q)
                    break
        
        return result