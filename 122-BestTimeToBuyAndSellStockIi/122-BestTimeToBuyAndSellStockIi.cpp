// Last updated: 2/12/2026, 3:45:33 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyIndex = 0;
        int profit = 0;
        for (int i = 1; prices.size() > i; i++) {
            if (prices[i] > prices[buyIndex]) {
                int sellPrice = prices[i] - prices[buyIndex];
                profit += sellPrice;
            }
            buyIndex = i;
        }
        return profit;
    }
};