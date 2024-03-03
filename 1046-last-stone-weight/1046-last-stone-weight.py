class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)

            if max1 != max2:
                heapq.heappush(stones, max1 - max2)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
