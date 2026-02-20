# Last updated: 2/19/2026, 7:09:47 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        house1 = 0
4        house2 = 0
5        for num in nums:
6            current = (max(house1, house2 + num))
7            house2 = house1
8            house1 = current
9        return house1