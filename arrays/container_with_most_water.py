# https://leetcode.com/problems/container-with-most-water/
# Similar problems:
# https://leetcode.com/problems/house-robber-iv/
# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) == 2:
            return min(height[0], height[1])

        max_area = 0
        p1 = 0
        p2 = len(height) - 1
        while p2 - p1 > 0:
            area = min(height[p1], height[p2]) * (p2 - p1)
            max_area = max(area, max_area)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area