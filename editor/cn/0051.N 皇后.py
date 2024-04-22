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
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯
        # 时间复杂度：
        # 空间复杂度：
        self.path = [["." for _ in range(n)] for _ in range(n)]  # 重点注意list引用问题，以后二维数组都这么写
        # self.path = ["." * n] * n   # 不能这么写
        self.result = []
        self.back_tracking(n, 0)
        return self.result

    def is_right(self, n, row, col):
        # 判断同行和同列
        for i in range(n):
            if self.path[row][i] == "Q":
                return False
            if self.path[i][col] == "Q":
                return False

        # # 判断斜线
        # for i in range(n):
        #     for j in range(n):
        #         if (i + j) == (row + col) and self.path[i][j] == "Q":
        #             return False
        #         if (i - row) == (j - col) and self.path[i][j] == "Q":
        #             return False
        # 检查左上方斜线
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.path[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 检查右上方斜线
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if self.path[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def back_tracking(self, n, row):
        # 终止条件
        if row == n:
            res_temp = []
            for i in range(n):
                res_temp.append("".join(self.path[i][:]))
            self.result.append(res_temp)
            return

        for i in range(n):
            if self.is_right(n, row, i):
                self.path[row][i] = "Q"
                self.back_tracking(n, row+1)
                self.path[row][i] = "."
# leetcode submit region end(Prohibit modification and deletion)
# s = Solution()
# res = s.solveNQueens(4)
# print(res)
