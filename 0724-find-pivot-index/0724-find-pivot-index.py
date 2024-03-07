class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = 0
        for num in nums:
            rightsum += num
            
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum -= nums[i]
            if rightsum == leftsum:
                return i
            
            leftsum += nums[i]
            
        return -1
        