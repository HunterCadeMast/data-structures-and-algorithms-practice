# Last updated: 2/18/2026, 10:14:31 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = []
4        group_sorted = []
5        for word in strs:
6            sorted_word = sorted(word)
7            if len(groups) == 0:
8                groups.append([word])
9                group_sorted.append(sorted_word)
10            else:
11                if sorted_word in group_sorted:
12                    group_index = group_sorted.index(sorted_word)
13                    groups[group_index].append(word)
14                else:
15                    groups.append([word])
16                    group_sorted.append(sorted_word)
17        return groups