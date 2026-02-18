# Last updated: 2/18/2026, 5:22:15 PM
1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        left = 0
4        right = len(heights) - 1
5        max_area = 0
6        while left < right:
7            area = min(heights[left], heights[right]) * (right - left)
8            max_area = max(max_area, area)
9            if heights[left] <= heights[right]:
10                left += 1
11            else:
12                right -= 1
13        return max_area