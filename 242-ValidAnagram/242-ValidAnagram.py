# Last updated: 2/12/2026, 3:45:26 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)