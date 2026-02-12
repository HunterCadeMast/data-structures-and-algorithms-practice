// Last updated: 2/12/2026, 3:45:30 PM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> checkSet;
        for(int num : nums) {
            if (checkSet.count(num)) {
                return true;
            }
            checkSet.insert(num);
        }
        return false;
    }
};