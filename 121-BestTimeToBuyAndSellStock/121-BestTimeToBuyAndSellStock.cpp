// Last updated: 2/12/2026, 3:45:34 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minCost = INT_MAX;
        int maxProfit = 0;
        for (int currentPrice : prices) {
            if (currentPrice < minCost) {
                minCost = currentPrice;
            }
            else {
                maxProfit = max(maxProfit, currentPrice - minCost);
            }
        }
        return maxProfit;
    }
};