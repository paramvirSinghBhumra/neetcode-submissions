class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_count = {}
        for num in nums:
            if num not in number_count:
                number_count[num] = 1
            else:
                if number_count[num]>1:
                    return False
                else:
                    return True
        return False

