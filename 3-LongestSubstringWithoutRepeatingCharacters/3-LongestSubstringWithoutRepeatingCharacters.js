// Last updated: 2/12/2026, 3:45:48 PM
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0, longest = 0, seen = new Set();
    for (let end = 0; s.length > end; end++) {
        let current = s[end];
        while (seen.has(current)) {
           seen.delete(s[start]);
           start++;
        }
        seen.add(current);
        longest = Math.max(longest, end - start + 1);
    }
    return longest;
};