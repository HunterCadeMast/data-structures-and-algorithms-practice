// Last updated: 2/12/2026, 3:45:24 PM
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> section;
        for (int i = 0; nums1.size() > i; i++) {
            for (int j = 0; nums2.size() > j; j++) {
                if (nums1[i] == nums2[j]) {
                    section.push_back(nums1[i]);
                    nums2.erase(nums2.begin() + j);
                    break;
                }
            }
        }
        return section;
    }
};