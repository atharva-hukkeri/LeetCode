class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            
            max2 = max(stones)
            stones.remove(max2)
            
            if max1 > max2:
                ele = max1 - max2
                stones.append(ele)
                
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
