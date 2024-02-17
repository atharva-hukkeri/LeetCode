class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = len(nums) - self.firstPositive(nums) 
        neg = self.lastNegative(nums) + 1
        
        return max(pos, neg)
        
    
    def lastNegative(self, nums):
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] < 0:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
                
        return ans
    
    def firstPositive(self, nums):
        start = 0
        end = len(nums) - 1
        ans = len(nums)
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] > 0:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
                
        return ans     
        