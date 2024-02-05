class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        elif nums[0] < nums[len(nums) - 1]:
            return nums[0]
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid != 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            elif mid != len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
                    
            elif nums[start] <= nums[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
                    
            
        
        