// Last updated: 2/12/2026, 3:45:26 PM
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
};