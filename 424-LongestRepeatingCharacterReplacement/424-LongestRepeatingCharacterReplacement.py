# Last updated: 2/12/2026, 3:45:23 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        seen = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            seen = max(seen, count[s[right]])
            while (right - left + 1) - seen > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result