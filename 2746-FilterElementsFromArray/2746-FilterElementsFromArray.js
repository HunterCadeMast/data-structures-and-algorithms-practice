// Last updated: 2/12/2026, 3:45:18 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let returnedArray = [];
    for (let i = 0; arr.length > i; i++) {
        if (fn(arr[i], i)) {
            returnedArray.push(arr[i]);
        };
    };
    return returnedArray;
};