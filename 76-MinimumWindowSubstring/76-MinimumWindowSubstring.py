# Last updated: 2/13/2026, 7:42:42 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5        while left <= right:
6            middle = (right + left) // 2
7            if nums[middle] == target:
8                return middle
9            if nums[left] <= nums[middle]:
10                if target > nums[middle] or target < nums[left]:
11                    left = middle + 1
12                else:
13                    right = middle - 1
14            else:
15                if target < nums[middle] or target > nums[right]:
16                    right = middle - 1
17                else:
18                    left = middle + 1
19        return -1