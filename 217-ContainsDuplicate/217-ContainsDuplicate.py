# Last updated: 2/12/2026, 3:45:27 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))