class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            
            remain = numBottles % numExchange
            
            ans = ans + newBottles
            
            numBottles = newBottles + remain
            
        return ans