class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = []
        
        for i in range(len(arr)):
            count = arr.count(arr[i])
            
            if count == arr[i]:
                ans.append(arr[i])
            else:
                ans.append(-1)
                
        return max(ans)
            
        
                