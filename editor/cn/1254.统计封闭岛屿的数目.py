# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。 
# 
#  请返回 封闭岛屿 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,
# 0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.grid = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.flag = True

    def closedIsland(self, grid: List[List[int]]) -> int:
        # 深搜 不能接触到边缘的岛屿即为封闭岛屿
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)

        m = len(grid)
        n = len(grid[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    self.dfs(grid, i, j)
                    if self.flag:
                        count += 1
                    self.flag = True
        return count

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])

        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y]:
            return

        grid[x][y] = 1
        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
            self.flag = False

        for x_offset, y_offset in self.grid:
            self.dfs(grid, x + x_offset, y + y_offset)
# leetcode submit region end(Prohibit modification and deletion)
