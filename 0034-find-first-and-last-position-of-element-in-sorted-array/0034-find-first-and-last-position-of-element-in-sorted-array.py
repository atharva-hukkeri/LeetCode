class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans
        
        ans[0] = self.First(nums,target)
        ans[1] = self.Last(nums,target)
        
        return ans

                
    def First(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        first = -1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                first = mid
                end = mid - 1
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                end = mid - 1
                
        return first
                
    def Last(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        last = -1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                last = mid
                start = mid + 1
            
            elif nums[mid] < target:
                start = mid + 1
            
            else:
                end = mid - 1
                
        return last