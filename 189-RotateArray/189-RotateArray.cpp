// Last updated: 2/12/2026, 3:45:32 PM
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        vector<int> temp(nums.size());
        for (int i = 0; nums.size() > i; i++) {
            temp[(i + k) % nums.size()] = nums[i];
        }
        nums = temp;
    }
};