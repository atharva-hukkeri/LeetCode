class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            ss = nums[start] * nums[start]
            es = nums[end] * nums[end]
            
            if ss > es:
                ans.append(ss)
                start += 1
            
            else:
                ans.append(es)
                end -= 1
                
        
        return ans[::-1]
        