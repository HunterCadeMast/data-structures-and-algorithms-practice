// Last updated: 2/12/2026, 3:45:16 PM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe : function(expected) {
            if (expected === val) {
                return true;
            }
            else {
                throw new Error("Not Equal");
            }
        },
        notToBe : function(expected) {
            if (expected !== val) {
                return true;
            }
            else {
                throw new Error("Equal");
            }
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */