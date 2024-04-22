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
        self.grid = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        # 广搜
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)
        island_num = 0
        x_end = len(grid)
        y_end = len(grid[0])
        for i in range(x_end):
            for j in range(y_end):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    island_num += 1
        return island_num

    def bfs(self, grid, x, y):
        x_end = len(grid)
        y_end = len(grid[0])

        queue = deque()
        queue.append((x, y))
        grid[x][y] = "0"
        while queue:
            cur_x, cur_y = queue.popleft()
            for x_offset, y_offset in self.grid:
                next_x = cur_x + x_offset
                next_y = cur_y + y_offset
                if next_x < 0 or next_y < 0 or next_x >= x_end \
                        or next_y >= y_end or grid[next_x][next_y] == "0":
                    continue
                else:
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = "0"

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # 深搜
    #     # 时间复杂度：O(n²)
    #     # 空间复杂度：
    #     island_num = 0
    #     x_end = len(grid)
    #     y_end = len(grid[0])
    #     for i in range(x_end):
    #         for j in range(y_end):
    #             if grid[i][j] == "1":
    #                 self.dfs(grid, i, j)
    #                 island_num += 1
    #     return island_num
    #
    # def dfs(self, grid, x, y):
    #     x_end = len(grid)
    #     y_end = len(grid[0])
    #     # 终止条件
    #     if x < 0 or y < 0 or x >= x_end or y >= y_end or grid[x][y] == "0":
    #         return
    #
    #     grid[x][y] = "0"
    #     for x_offset, y_offset in self.grid:
    #         self.dfs(grid, x+x_offset, y+y_offset)
# leetcode submit region end(Prohibit modification and deletion)
