# Last updated: 2/12/2026, 3:45:46 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = 0
        seen = []
        if s == " ":
            return 1
        for letter in s:
            if letter in seen:
                sub = max(sub, len(seen))
                index = seen.index(letter)
                seen = seen[index + 1:]
                seen.append(letter)
            else:
                seen.append(letter)
        return max(sub, len(seen))