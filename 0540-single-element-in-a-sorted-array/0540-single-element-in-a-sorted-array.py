class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            elif mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 1
                    
                else:
                    end = mid - 1
                
            else:
                if nums[mid] == nums[mid - 1]:
                    start = start + 1
                    
                else:
                    end = mid - 1
                    
        return -1