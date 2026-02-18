class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        target_count = 0

        for i in hours:
            if i == target or i > target:
                target_count += 1
        return target_count