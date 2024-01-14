class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        fterm = 0
        sterm = 1
        
        for i in range(n):
            thirdterm = fterm + sterm
            
            fterm = sterm
            sterm = thirdterm
            
        return fterm
        