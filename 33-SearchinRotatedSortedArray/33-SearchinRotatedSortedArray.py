# Last updated: 2/15/2026, 2:35:02 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        frequent_nums = []
4        frequency = []
5        nums_set = set(nums)
6        for num in nums_set:
7            num_count = nums.count(num)
8            if len(frequent_nums) < k:
9                frequent_nums.append(num)
10                frequency.append(num_count)
11            else:
12                minimum = min(frequency)
13                if num_count > minimum:
14                    frequent_nums[frequency.index(minimum)] = num
15                    frequency[frequency.index(minimum)] = num_count
16        return frequent_nums