class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        if digits[n - 1] != 9:
            digits[n - 1] += 1
            return digits
        
        digits[n - 1] = 0
        
        for i in range(n-2, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            
        # digits.insert(0, 1)
        return [1] + digits
        