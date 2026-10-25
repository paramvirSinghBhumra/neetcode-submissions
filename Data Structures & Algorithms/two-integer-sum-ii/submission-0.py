class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while (l < r and l < len(numbers)-1 and r >= 0):
            summation = numbers[l] + numbers[r]

            if summation < target: 
                l += 1
            elif summation > target:
                r -= 1
            else:
                break

        return [l+1,r+1]