class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currSum += nums[i]
                
            else:
                maxSum = max(currSum, maxSum)
                currSum = nums[i]
                
        maxSum = max(currSum, maxSum)         
        return maxSum