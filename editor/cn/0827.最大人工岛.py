# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。 
# 
#  返回执行此操作后，grid 中最大的岛屿面积是多少？ 
# 
#  岛屿 由一组上、下、左、右四个方向相连的 1 形成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
#  
# 
#  示例 2: 
# 
#  
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。 
# 
#  示例 3: 
# 
#  
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。 
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 500 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 407 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.grid = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.island_index = 0
        self.island_cnt = 0

    def largestIsland(self, grid: List[List[int]]) -> int:
        # 深搜
        # 时间复杂度：O(mn)
        # 空间复杂度：O(mn)
        x_end = len(grid)
        y_end = len(grid[0])

        visited = [[False for _ in range(y_end)] for _ in range(x_end)]
        island_index_map = [[-1 for _ in range(y_end)] for _ in range(x_end)]
        island_area = []
        max_area = -1

        # 统计各个岛屿面积
        for i in range(x_end):
            for j in range(y_end):
                if grid[i][j] and not visited[i][j]:
                    self.dfs(grid, i, j, visited, island_index_map)
                    island_area.append(self.island_cnt)
                    max_area = max(self.island_cnt, max_area)
                    self.island_index += 1
                    self.island_cnt = 0

        # 计算补1后最大岛屿面积
        for i in range(x_end):
            for j in range(y_end):
                if not grid[i][j]:
                    cur_area = 1
                    near_island_index = []
                    for x_offset, y_offset in self.grid:
                        next_x = i + x_offset
                        next_y = j + y_offset
                        if 0 <= next_x < x_end and 0 <= next_y < y_end and \
                                grid[next_x][next_y]:
                            island_index = island_index_map[next_x][next_y]
                            if island_index not in near_island_index:
                                near_island_index.append(island_index)
                                cur_area += island_area[island_index]
                    max_area = max(max_area, cur_area)
        return max_area

    def dfs(self, grid, x, y, visited, island_index_map):
        x_end = len(grid)
        y_end = len(grid[0])

        if x < 0 or x >= x_end or y < 0 or y >= y_end or \
                visited[x][y] or not grid[x][y]:
            return

        visited[x][y] = True
        self.island_cnt += 1
        island_index_map[x][y] = self.island_index

        for x_offset, y_offset in self.grid:
            self.dfs(grid, x+x_offset, y+y_offset, visited, island_index_map)
# leetcode submit region end(Prohibit modification and deletion)
