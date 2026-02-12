// Last updated: 2/12/2026, 3:45:39 PM
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int row = 0; board.size() > row; row++) {
            unordered_set<char> rowSeen;
            unordered_set<char> columnSeen;
            for (int column = 0; board.size() > column; column++) {
                if (board[row][column] != '.') {
                    if (rowSeen.count(board[row][column])) {
                        return false;
                    }
                    rowSeen.insert(board[row][column]);
                }
                if (board[column][row] != '.') {
                    if (columnSeen.count(board[column][row])) {
                        return false;
                    }
                    columnSeen.insert(board[column][row]);
                }
            }
        }
        for (int boxRow = 0; boxRow < 3; boxRow++) {
            for (int boxColumn = 0; boxColumn < 3; boxColumn++) {
                unordered_set<char> boxSeen;
                for (int row = 0; row < 3; row++) {
                    for (int column = 0; column < 3; column++) {
                        if (board[boxRow * 3 + row][boxColumn * 3 + column] != '.') {
                            if (boxSeen.count(board[boxRow * 3 + row][boxColumn * 3 + column])) {
                                return false;
                            }
                            boxSeen.insert(board[boxRow * 3 + row][boxColumn * 3 + column]);
                        }
                    }
                }
            }
        }
        return true;
    }
};