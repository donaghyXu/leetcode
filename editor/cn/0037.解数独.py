# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  数独的解法需 遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  数独部分空格内已填入了数字，空白格用 '.' 表示。 
# 
#  
# 
#  
#  
#  
#  示例 1： 
#  
#  
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".
# ",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".
# ","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6
# "],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[
# ".",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8
# "],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],[
# "4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9",
# "6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4",
# "5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#  
#  
#  
#  
# 
# 
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字或者 '.' 
#  题目数据 保证 输入数独仅有一个解 
#  
# 
#  Related Topics 数组 哈希表 回溯 矩阵 👍 1819 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 回溯
        # 时间复杂度：O(9^(9x9))，较为宽松的一个上界，具体取决于输入数据
        # 空间复杂度：O(1)
        self.back_tracking(board)

    def is_valid(self, board, row, col, k):
        # 判断行和列
        if str(k) in board[row]:
            return False
        for i in range(len(board)):
            if str(k) == board[i][col]:
                return False

        # 判断九宫格
        grid_x_index = int(row / 3)
        grid_y_index = int(col / 3)
        for i in range(3):
            for j in range(3):
                x = grid_x_index * 3 + i
                y = grid_y_index * 3 + j
                if str(k) == board[x][y]:
                    return False
        return True

    def back_tracking(self, board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    continue
                for k in range(1, 10):
                    if self.is_valid(board, i, j, k):
                        board[i][j] = str(k)
                        if self.back_tracking(board):
                            return True
                        board[i][j] = '.'
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
