class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        right = []
        pro = 1
        
        for i in range(n-1, -1, -1):
            pro = pro * nums[i]
            right.append(pro)
        
        right = right[::-1]
            
        left = 1
        
        for i in range(n-1):
            val = left * right[i+1]
            ans.append(val)
            
            left = left * nums[i]
            
        ans.append(left)
        
        return ans
        