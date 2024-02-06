class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[len(nums) - 1] > nums[len(nums) - 2]:
            return (len(nums)-1)
        
        start = 1
        end = len(nums) - 2
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            
            elif nums[mid + 1] > nums[mid]:
                start = start + 1
                
            else:
                end = end - 1