# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2473 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List
class Solution:
    def __init__(self):
        self.grid = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        # 深搜
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)

        m = len(grid)
        n = len(grid[0])
        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    island_num += 1
        return island_num

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        # 终止条件
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
            return

        grid[x][y] = "0"
        for x_offset, y_offset in self.grid:
            self.dfs(grid, x + x_offset, y + y_offset)
# leetcode submit region end(Prohibit modification and deletion)
