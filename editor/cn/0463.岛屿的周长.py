# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。 
# 
#  网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。 
# 
#  岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿
# 的周长。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# 输出：16
# 解释：它的周长是上面图片中的 16 个黄色的边 
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1]]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,0]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  row == grid.length 
#  col == grid[i].length 
#  1 <= row, col <= 100 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 746 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 遍历
        # 时间复杂度：O(mn)
        # 空间复杂度：O(1)
        # 思路：只计算当前陆地的下方和右方是否是陆地，如果是的话，那么有重叠的边，计数，在后面去除
        #      每个陆地只看下方和右方是考虑循环不变量，不影响其他陆地

        m = len(grid)
        n = len(grid[0])
        island_cnt = 0
        cover_cnt = 0
        dir = [(1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    island_cnt += 1
                    for x_offset, y_offset in dir:
                        x = i + x_offset
                        y = j + y_offset
                        if 0 <= x < m and 0 <= y < n and grid[x][y]:
                            cover_cnt += 1
        return 4 * island_cnt - 2 * cover_cnt
# leetcode submit region end(Prohibit modification and deletion)
