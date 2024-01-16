class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        totalele = len(nums)
        
        ans = []
        for i in range(totalele):
            for j in range(i+1, totalele):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    
        return ans