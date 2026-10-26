class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total_sum = 0
        multiplier = 1

        for i in range(len(digits)-1,-1,-1):
            total_sum += digits[i]*multiplier
            multiplier *= 10
        
        total_sum += 1

        arr = []
        for i in str(total_sum):
            arr.append(i)
        
        return arr