# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。 
# 
#  n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 数组 回溯 👍 2068 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯
        # 时间复杂度：O(n!)
        # 空间复杂度：O(n²)

        board = [["." for _ in range(n)] for _ in range(n)]
        self.back_tracking(board, 0)
        return self.result

    def back_tracking(self, board, row):
        # 终止条件
        if row == len(board):
            self.result.append(["".join(x) for x in board])
            return

        for col in range(len(board)):
            if board[row][col] == "." and self.is_valid(board, row, col):
                board[row][col] = "Q"
                self.back_tracking(board, row + 1)
                board[row][col] = "."

    def is_valid(self, board, x, y):
        # 同列
        for row in range(x):
            if board[row][y] == "Q":
                return False

        # 同斜线
        row = x - 1
        col = y - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row = x - 1
        col = y + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
