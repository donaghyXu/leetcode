# 在给定的 m x n 网格
#  grid 中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。 
# 
#  返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
# 
#  Related Topics 广度优先搜索 数组 矩阵 👍 889 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.one_num = 0

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # 时间复杂度：O(mn)
        # 空间复杂度：O(mn)
        min_minute = 0
        m = len(grid)
        n = len(grid[0])

        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.one_num += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            if self.one_num == 0:
                return min_minute

            min_minute += 1
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                self.trans(grid, x, y, queue)

        if self.one_num > 0:
            return -1
        return min_minute

    def trans(self, grid, x, y, queue):
        m = len(grid)
        n = len(grid[0])
        for x_offset, y_offset in self.dir:
            x_new = x + x_offset
            y_new = y + y_offset
            if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] == 1:
                self.one_num -= 1
                grid[x_new][y_new] = 2
                queue.append((x_new, y_new))
# leetcode submit region end(Prohibit modification and deletion)
