# Last updated: 2/12/2026, 3:45:29 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated = nums.copy()
        for i in range(len(nums)):
            rotated[(k + i) % len(nums)] = nums[i]
        nums[:] = rotated