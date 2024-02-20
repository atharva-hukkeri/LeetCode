class Solution:
    def average(self, salary: List[int]) -> float:
        maxSal = salary[0]
        minSal = salary[0]
        sumSal = 0
        
        for i in range(len(salary)):
            if salary[i] > maxSal:
                maxSal = salary[i]
            elif salary[i] < minSal:
                minSal = salary[i]
            
            sumSal += salary[i]
            
                
        avgSal = (sumSal - maxSal - minSal) / (len(salary) - 2)
        return avgSal
            
        
        