# Last updated: 2/13/2026, 7:34:59 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left < right:
6            middle = left + (right - left) // 2
7            if nums[middle] < nums[right]:
8                right = middle
9            else:
10                left = middle + 1
11        return nums[left]