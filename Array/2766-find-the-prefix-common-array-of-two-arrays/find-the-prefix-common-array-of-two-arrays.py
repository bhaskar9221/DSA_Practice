class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
      
        frequency_a = Counter()
      
        frequency_b = Counter()
      
        for element_a, element_b in zip(A, B):
            frequency_a[element_a] += 1
            frequency_b[element_b] += 1
          
            common_count = sum(
                min(freq_in_a, frequency_b[element]) 
                for element, freq_in_a in frequency_a.items()
            )
          
            result.append(common_count)
      
        return result