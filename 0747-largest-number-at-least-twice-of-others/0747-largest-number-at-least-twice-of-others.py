class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        big = max(nums)
        big_in = nums.index(big)
        
        for i in range(len(nums)):
            if i != big_in and nums[i] * 2 > big:
                return -1   
            
        return big_in
                