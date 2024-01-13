class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        revnum = 0

        while num > 0:
            lastd = num % 10
            revnum = revnum*10 + lastd

            num = num//10

        if revnum == x:
            return True
        else:
            return False

        