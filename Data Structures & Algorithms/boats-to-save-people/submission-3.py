class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boat_count = 0

        while i <= j:
            weight = people[i] + people[j]
            
            if weight <= limit:
                i += 1
            j -= 1
            boat_count += 1
        return boat_count