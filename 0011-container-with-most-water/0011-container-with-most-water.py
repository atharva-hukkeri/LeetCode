class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        maxCap = 0
        
        while start < end:
            length = min(height[start], height[end])
            breadth = end - start
            
            volumne = length * breadth
            maxCap = max(volumne, maxCap)
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return maxCap