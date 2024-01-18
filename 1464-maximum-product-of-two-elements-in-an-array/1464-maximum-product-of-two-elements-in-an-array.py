class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mul_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                mul = (nums[i]-1) * (nums[j]-1)
                mul_list.append(mul)
                
        return max(mul_list)
        