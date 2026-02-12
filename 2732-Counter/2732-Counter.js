// Last updated: 2/12/2026, 3:45:19 PM
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var firstFlag = true;
    return function() {
        if (firstFlag == true) {
            firstFlag = false
            return n;
        }
        else {
            return n += 1;
        }
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */