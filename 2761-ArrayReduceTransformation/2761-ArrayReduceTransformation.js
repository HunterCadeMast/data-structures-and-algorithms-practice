// Last updated: 2/12/2026, 3:45:15 PM
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length === 0) {
        return init;
    };
    let val = 0;
    for (let i = 0; nums.length > i; i++) {
        if (i === 0) {
            val = fn(init, nums[0]);
        }
        else {
            val = fn(val, nums[i]);
        };
    };
    return val
};