# Last updated: 2/12/2026, 3:45:40 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        used = [False] * len(nums)
        def recurse(rest : List[int]):
            if (len(rest) == len(nums)):
                combinations.append(rest[:])
                return
            i = 0
            while len(nums) > i:
                if (used[i]):
                    i += 1
                    continue
                rest.append(nums[i])
                used[i] = True
                recurse(rest)
                rest.pop()
                used[i] = False
                i += 1
        recurse([])
        return combinations