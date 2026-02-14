# Last updated: 2/13/2026, 7:13:08 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not s or not t:
4            return ""
5        count = {}
6        for letter in t:
7            count[letter] = count.get(letter, 0) + 1
8        left = 0
9        min_length = float("inf")
10        result = (0, 0)
11        missing = len(t)
12        for right, letter in enumerate(s):
13            if letter in count:
14                if count[letter] > 0:
15                    missing -= 1
16                count[letter] -= 1
17            while missing == 0:
18                if right - left + 1 < min_length:
19                    min_length = right - left + 1
20                    result = (left, right)
21                left_letter = s[left]
22                if left_letter in count:
23                    count[left_letter] += 1
24                    if count[left_letter] > 0:
25                        missing += 1
26                left += 1
27        l, r = result
28        return s[l:r + 1] if min_length != float("inf") else ""