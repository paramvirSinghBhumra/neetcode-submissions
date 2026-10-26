class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n

        while(num not in visited):
            visited.add(num)
            
            str_num = str(num)
            total_sum = 0
            for nn in str_num:
                total_sum += (int(nn)**2)
            
            num = total_sum
            if num == 1:
                return True
        
        return False
            