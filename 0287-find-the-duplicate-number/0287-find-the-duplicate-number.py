class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ele = abs(nums[i])
            
            if nums[ele] > 0:
                nums[ele] = -nums[ele]
                
            else:
                return ele
                