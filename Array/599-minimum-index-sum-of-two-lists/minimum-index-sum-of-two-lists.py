class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_map = {name: i for i,name in enumerate(list1)}
        result = []
        min_sum = float('inf')

        for j,name in enumerate(list2):
            if name in list1_map:
                current_sum = list1_map[name] + j

                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [name]
                elif current_sum == min_sum:
                    result.append(name)
        return result