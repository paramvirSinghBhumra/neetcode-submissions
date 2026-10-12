class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            diff = target - nums[first]
            for second in range(first + 1, len(nums)):
                if nums[second] == diff:
                    return [first, second]

        return [-1,-1]