# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。 
# 
#  一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。 
# 
#  返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#  
# 
#  示例 2： 
#  
#  
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 500 
#  grid[i][j] 的值为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 269 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.count = 0
        self.flag = False
        self.grid = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 深搜
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    if not self.flag:
                        result += self.count
                    self.count = 0
                    self.flag = False
        return result

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n or not grid[x][y]:
            return

        grid[x][y] = 0
        self.count += 1
        if x == 0 or x == (m - 1) or y == 0 or y == (n - 1):
            self.flag = True

        for x_offset, y_offset in self.grid:
            self.dfs(grid, x + x_offset, y + y_offset)
# leetcode submit region end(Prohibit modification and deletion)
