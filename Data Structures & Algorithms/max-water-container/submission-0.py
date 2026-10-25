class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1

        max_area = -1
        while (left < right):
            l, r = heights[left], heights[right]
            area_calculation = min(l,r) * (right-left)

            max_area = area_calculation if area_calculation > max_area else max_area

            if l > r:
                right -=1
            else:
                left += 1

        return max_area