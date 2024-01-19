class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        
        ActualSum = (size * (size + 1)) // 2
        
        CurrentSum = 0
        
        for i in range(size):
            CurrentSum = CurrentSum + nums[i]
        
        ans = ActualSum - CurrentSum
        
        return ans
        