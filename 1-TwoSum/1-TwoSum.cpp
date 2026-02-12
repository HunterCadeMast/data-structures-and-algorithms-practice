// Last updated: 2/12/2026, 3:45:45 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output(2, 0);
        for (int currentNum = 0, nextNum = 1; currentNum <= nums.size(); nextNum++) {
            if (nums[currentNum] + nums[nextNum] == target) {
                output[0] = currentNum;
                output[1] = nextNum;
                return output;
            }
            else if ((nextNum + 1) == nums.size()) {
                currentNum++;
                nextNum = currentNum;
            }
        }
        return output;
    }
};