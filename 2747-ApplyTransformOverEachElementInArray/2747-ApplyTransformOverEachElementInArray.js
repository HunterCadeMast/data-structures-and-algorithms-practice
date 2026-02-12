// Last updated: 2/12/2026, 3:45:17 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let returnedArray = [];
    for (let i = 0; arr.length > i; i++) {
        returnedArray[i] = fn(arr[i], i);
    };
    return returnedArray;
};