# Last updated: 2/15/2026, 2:33:34 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for i in range(len(nums)):
4            for j in range(i + 1, len(nums)):
5                if nums[i] + nums[j] == target:
6                    return [i, j]