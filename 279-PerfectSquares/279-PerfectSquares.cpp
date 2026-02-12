// Last updated: 2/12/2026, 3:45:25 PM
class Solution {
public:
    int numSquares(int n) {
        static vector<int> count {0};
        while (count.size() <= n) {
            int m = count.size(), squares = INT_MAX;
            for (int i = 1; i * i <= m; i++) {
                squares = min(squares, count[m - i * i] + 1);
            }
            count.push_back(squares);
        }
        return count[n];
    }
};