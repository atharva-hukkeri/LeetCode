class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        
        for n in nums_set:
            if (n - 1) not in nums_set:
                k = 1
                while (n + k) in nums_set:
                    k += 1
                    
                ans = max(ans, k)
                
        return ans
