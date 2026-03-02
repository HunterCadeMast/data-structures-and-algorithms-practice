// Last updated: 3/2/2026, 4:48:03 PM
1class Solution {
2public:
3    bool containsDuplicate(vector<int>& nums) {
4        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
5    }
6};