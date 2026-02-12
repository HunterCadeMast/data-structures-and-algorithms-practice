# Last updated: 2/12/2026, 3:45:28 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num not in seen:
                if nums.count(num) > (len(nums) / 2):
                    return num
                else:
                    seen.append(num)