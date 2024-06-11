# 给你一个大小为 m x n 的二进制矩阵 grid 。 
# 
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。 
# 
#  岛屿的面积是岛上值为 1 的单元格的数目。 
# 
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,
# 0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,
# 0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1065 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.dir = [(0,-1), (0, 1), (-1, 0), (1, 0)]
        self.count = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 2.深搜
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n²)
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.dfs(grid, i, j)
                    max_area = max(max_area, self.count)
                    self.count = 0
        return max_area

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n or not grid[x][y]:
            return

        grid[x][y] = 0
        self.count += 1
        for x_offset, y_offset in self.dir:
            self.dfs(grid, x+x_offset, y+y_offset)

    # def __init__(self):
    #     self.dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    #     self.count = 0
    #
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     # 1.广搜
    #     # 时间复杂度：O(n²)
    #     # 空间复杂度：O(1)
    #     max_island_area = 0
    #     x_end = len(grid)
    #     y_end = len(grid[0])
    #     for i in range(x_end):
    #         for j in range(y_end):
    #             if grid[i][j]:
    #                 self.bfs(grid, i, j)
    #                 max_island_area = max(max_island_area, self.count)
    #                 self.count = 0
    #     return max_island_area
    #
    # def bfs(self, grid, x, y):
    #     x_end = len(grid)
    #     y_end = len(grid[0])
    #
    #     queue = collections.deque()
    #     queue.append((x, y))
    #     grid[x][y] = 0
    #     self.count += 1
    #     while queue:
    #         cur_x, cur_y = queue.popleft()
    #         for x_offset, y_offset in self.dir:
    #             next_x = cur_x + x_offset
    #             next_y = cur_y + y_offset
    #             if 0 <= next_x < x_end and 0 <= next_y < y_end and \
    #                     grid[next_x][next_y]:
    #                 queue.append((next_x, next_y))
    #                 grid[next_x][next_y] = 0
    #                 self.count += 1
# leetcode submit region end(Prohibit modification and deletion)
