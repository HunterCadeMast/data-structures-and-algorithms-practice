// Last updated: 2/12/2026, 3:45:47 PM
#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int longest = 0;
        unordered_set<char> seen;
        for (int end = 0; end < s.length(); end++) {
            char currentChar = s[end];
            while (seen.count(currentChar) > 0) {
                seen.erase(s[start]);
                start++;
            }
            seen.insert(currentChar);
            longest = max(longest, end - start + 1);
        }
        return longest;
    }
};