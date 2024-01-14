class Solution:
    def tribonacci(self, n: int) -> int:   
        firstnum = 0
        secondnum = 1
        thirdnum = 1
        
        for i in range(n):
            forthnum = firstnum + secondnum + thirdnum
            
            firstnum = secondnum
            secondnum = thirdnum
            thirdnum = forthnum
            
        return firstnum
        