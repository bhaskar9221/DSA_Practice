class Solution:
    def secondHighest(self, s: str) -> int:
        largest = second_largest = -1

        for c in s:
            if c.isdigit():
                num = int(c)

                if num>largest: 
                    second_largest = largest
                    largest = num
                elif largest>num>second_largest:
                    second_largest = num
        return second_largest