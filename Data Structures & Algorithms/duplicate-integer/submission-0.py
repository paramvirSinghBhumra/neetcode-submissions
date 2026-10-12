class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_list = set(nums)

        return len(nums) != len(set_list)
        