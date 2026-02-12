// Last updated: 2/12/2026, 3:45:37 PM
class Solution {
public:
    int climbStairs(int n) {
        vector<int>ways(n + 1);
        ways[0] = 1;
        ways[1] = 1;
        for (int i = 2; i <= n; i++) {
            ways[i] = ways[i - 1] + ways[i - 2];
        }
        return ways[n];
    }
};