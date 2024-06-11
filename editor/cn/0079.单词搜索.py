# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCCED"
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "SEE"
# 输出：true
#  
# 
#  示例 3： 
#  
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCB"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？ 
# 
#  Related Topics 数组 字符串 回溯 矩阵 👍 1827 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.path = []
        self.result = []

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 回溯
        # 时间复杂度：O(mn * 3^L)，L为word的长度
        # 空间复杂度：O(mn)

        m = len(board)
        n = len(board[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    result = self.back_tracking(board, i, j, word, used)
                    if result:
                        return True
        return False

    def back_tracking(self, board, x, y, word, used):
        if len(self.path) == len(word):
            return True
        m = len(board)
        n = len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or used[x][y]:
            return False

        path_len = len(self.path)
        if board[x][y] == word[path_len]:
            self.path.append(board[x][y])
            used[x][y] = True
            for x_offset, y_offset in self.dir:
                if self.back_tracking(board, x + x_offset, y + y_offset, word, used):
                    return True
            used[x][y] = False
            self.path.pop()
        return False
# leetcode submit region end(Prohibit modification and deletion)
