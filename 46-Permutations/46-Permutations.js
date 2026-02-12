// Last updated: 2/12/2026, 3:45:42 PM
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const totalCombinations = [];
    const used = new Array(nums.length).fill(false);
    function recurse(rest) {
        if (rest.length === nums.length) {
            totalCombinations.push([...rest]);
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            rest.push(nums[i]);
            recurse(rest);
            rest.pop();
            used[i] = false;
        }
    }
    recurse([]);
    return totalCombinations;
};