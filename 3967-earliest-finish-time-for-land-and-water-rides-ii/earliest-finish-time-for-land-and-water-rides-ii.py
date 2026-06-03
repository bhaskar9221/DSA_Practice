class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], 
                           waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        min_land_finish = float('inf')
        min_water_finish = float('inf')
        
        for start, dur in zip(landStartTime, landDuration):
            min_land_finish = min(min_land_finish, start + dur)
            
        for start, dur in zip(waterStartTime, waterDuration):
            min_water_finish = min(min_water_finish, start + dur)
            
        ans = float('inf')
        
        for w_start, w_dur in zip(waterStartTime, waterDuration):
            ans = min(ans, max(min_land_finish, w_start) + w_dur)
            
        for l_start, l_dur in zip(landStartTime, landDuration):
            ans = min(ans, max(min_water_finish, l_start) + l_dur)
            
        return ans
