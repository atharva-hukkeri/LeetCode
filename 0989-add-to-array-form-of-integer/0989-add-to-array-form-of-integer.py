class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        
        p = len(num) - 1
        carry = 0
        
        while p >= 0 or k > 0:
            numval = 0
            
            if p >= 0:
                numval = num[p]
            
            d = k % 10
            
            add = numval + d + carry
            
            digit = add % 10
            carry = add//10
            
            ans.append(digit)
            
            p -= 1
            k = k//10
        
        if carry > 0:
            ans.append(carry)
        
        ans = ans[::-1]
        return ans