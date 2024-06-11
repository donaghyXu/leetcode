# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.flag = True
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.modify_res = []

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 深搜
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n²)
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    self.dfs(board, i, j, visited)
                    if self.flag:
                        for x, y in self.modify_res:
                            board[x][y] = "X"
                    self.flag = True
                    self.modify_res = []

    def dfs(self, board, x, y, visited):
        m = len(board)
        n = len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or \
                visited[x][y] or board[x][y] == "X":
            return

        visited[x][y] = True
        self.modify_res.append([x, y])
        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
            self.flag = False
        for x_offset, y_offset in self.dir:
            self.dfs(board, x + x_offset, y + y_offset, visited)
# leetcode submit region end(Prohibit modification and deletion)