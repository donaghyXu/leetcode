# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 模拟
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)

        # 循环圈数
        loop = int(n / 2)
        # 起始坐标
        x_start = 0
        y_start = 0
        # 循环不变量的偏移量
        offset = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1

        while loop:
            # 计算上方行
            y_end = y_start + n - offset
            for i in range(y_start, y_end):
                matrix[x_start][i] = num
                num += 1

            # 计算右侧列
            x_end = x_start + n - offset
            for i in range(x_start, x_end):
                matrix[i][y_end] = num
                num += 1

            # 计算下方行
            for i in range(y_end, y_start, -1):
                matrix[x_end][i] = num
                num += 1

            # 计算左侧列
            for i in range(x_end, x_start, -1):
                matrix[i][y_start] = num
                num += 1

            loop -= 1
            x_start += 1
            y_start += 1
            offset += 2

        # 如果是奇数矩阵，计算落单的中心数
        if n % 2:
            matrix[x_start][y_start] = num
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
