// Last updated: 2/12/2026, 3:45:38 PM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        double current = 0.0;
        double best = 1.0 / -0.0;
        for (int number : nums) {
            current += number;
            best = std::max(best, current);
            if (current < 0.0) {
                current = 0.0;
            }
        }
        return best;
    }
};