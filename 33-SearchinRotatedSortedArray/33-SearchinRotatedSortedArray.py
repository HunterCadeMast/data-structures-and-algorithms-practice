# Last updated: 2/15/2026, 2:32:17 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums_set = set(nums)
4        if len(nums_set) == len(nums):
5            return False
6        return True