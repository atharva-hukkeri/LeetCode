class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        tcount = 0
        small_nums = 0
        
        for num in nums:
            if num == target:
                tcount += 1
            elif num < target:
                small_nums += 1
                
        ans = []
                
        while tcount > 0:
            ans.append(small_nums)
            small_nums += 1
            tcount -= 1
            
        return ans
        