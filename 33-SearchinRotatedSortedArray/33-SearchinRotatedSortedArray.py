# Last updated: 2/15/2026, 2:32:59 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return sorted(s) == sorted(t)