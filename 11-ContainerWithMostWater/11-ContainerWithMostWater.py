# Last updated: 2/18/2026, 5:47:32 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        results = []
4        total_product = 1
5        zero_check = nums.count(0)
6        if zero_check >= 2:
7            for i in range(len(nums)):
8                results.append(0)
9            return results
10        for num in nums:
11            if num != 1 and num != 0:
12                total_product = total_product * num
13        for i in range(len(nums)):
14            if nums[i] == 0:
15                results.append(total_product)
16            elif nums[i] != 0 and zero_check > 0:
17                results.append(0)
18            else:
19                results.append(total_product // nums[i])
20        return results