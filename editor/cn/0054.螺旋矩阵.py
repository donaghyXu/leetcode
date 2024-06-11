# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1662 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 模拟
        # 时间复杂度：O(mn)
        # 空间复杂度：O(mn)
        m = len(matrix)
        n = len(matrix[0])
        
        min_num = min(m, n)
        # 循环圈数
        loop = int(min_num / 2)
        # 循环不变量的偏移量
        offset = 1
        # 起始坐标
        x_start = 0
        y_start = 0

        result = []
        while loop:
            # 计算上方行
            y_end = y_start + n - offset
            for i in range(y_start, y_end):
                result.append(matrix[x_start][i])

            # 计算右侧列
            x_end = x_start + m - offset
            for i in range(x_start, x_end):
                result.append(matrix[i][y_end])

            # 计算下方行
            for i in range(y_end, y_start, -1):
                result.append(matrix[x_end][i])

            # 计算左侧列
            for i in range(x_end, x_start, -1):
                result.append(matrix[i][y_start])

            loop -= 1
            x_start += 1
            y_start += 1
            offset += 2

        # 根据最小行或列的奇偶情况，计算中心位置落单的行或列
        if min_num % 2:
            if m < n:
                for i in range(y_start, y_start + n - offset + 1):
                    result.append(matrix[x_start][i])
            else:
                for i in range(x_start, x_start + m - offset + 1):
                    result.append(matrix[i][y_start])
        return result
# leetcode submit region end(Prohibit modification and deletion)
