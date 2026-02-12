// Last updated: 2/12/2026, 3:45:43 PM
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int k = 1;
        for(int i = 1; nums.size() > i; i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};