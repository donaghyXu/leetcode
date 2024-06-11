# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 
# 
#  这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上
# 单元格 高于海平面的高度 。 
# 
#  岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 
# 
#  返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可
# 流向大西洋 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == heights.length 
#  n == heights[r].length 
#  1 <= m, n <= 200 
#  0 <= heights[r][c] <= 10⁵ 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 685 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.grid = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 深搜 优化版本
        # 时间复杂度：O(m*n)  第一次从太平洋出发mn，第二次从大西洋出发mn，遍历结果mn
        # 空间复杂度：O(mn)
        result = []
        x_end = len(heights)
        y_end = len(heights[0])

        visited_pacific = [[False for i in range(y_end)] for j in range(x_end)]
        # 从太平洋出发
        for i in range(x_end):
            visited_pacific[i][0] = True
            self.dfs(heights, i, 0, visited_pacific)
        for i in range(y_end):
            visited_pacific[0][i] = True
            self.dfs(heights, 0, i, visited_pacific)

        visited_atlantic = [[False for i in range(y_end)] for j in range(x_end)]
        # 从大西洋出发
        for i in range(x_end):
            visited_atlantic[i][y_end - 1] = True
            self.dfs(heights, i, y_end - 1, visited_atlantic)
        for i in range(y_end):
            visited_atlantic[x_end - 1][i] = True
            self.dfs(heights, x_end - 1, i, visited_atlantic)

        for i in range(x_end):
            for j in range(y_end):
                if visited_atlantic[i][j] and visited_pacific[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, heights, x, y, visited):
        x_end = len(heights)
        y_end = len(heights[0])

        # 单层处理逻辑
        for x_offset, y_offset in self.grid:
            next_x = x + x_offset
            next_y = y + y_offset
            if 0 <= next_x < x_end and 0 <= next_y < y_end and \
                    not visited[next_x][next_y] and \
                    heights[next_x][next_y] >= heights[x][y]:
                visited[next_x][next_y] = True
                self.dfs(heights, next_x, next_y, visited)
# leetcode submit region end(Prohibit modification and deletion)
