class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        firstnum = 0
        secondnum = 1
        thirdnum = 1
        
        for i in range(n):
            forthnum = firstnum + secondnum + thirdnum
            
            firstnum = secondnum
            secondnum = thirdnum
            thirdnum = forthnum
            
        return firstnum
        