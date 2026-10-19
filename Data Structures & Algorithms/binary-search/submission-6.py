class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right = 0, size
        mid = right//2

        while (left <= right) and mid < size:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
            mid = (left+right)//2

        if size == 1 and nums[0] == target:
            return 0
        return -1