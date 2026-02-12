# Last updated: 2/12/2026, 3:45:22 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]