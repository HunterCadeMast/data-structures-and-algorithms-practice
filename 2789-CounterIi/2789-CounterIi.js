// Last updated: 2/12/2026, 3:45:14 PM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const resetInit = init
    return {
        increment : function() {
            return init += 1
        },
        decrement : function() {
            return init -= 1
        },
        reset : function() {
            return init = resetInit
        }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */