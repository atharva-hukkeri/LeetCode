class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float(inf)
        second = float(inf)
        third = float(inf)
        
        for i in range(len(nums)):
            ele = nums[i]
            
            if first >= ele:
                first = ele
            elif second >= ele:
                second = ele
            else:
                third = ele
                return True
            
        return False