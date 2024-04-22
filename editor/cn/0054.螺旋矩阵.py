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
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n²)
        x_start = 0
        y_start = 0
        x_len = len(matrix)
        y_len = len(matrix[0])
        n = min(x_len, y_len)
        loop = int(n / 2)
        mid = loop
        sub_len = 1
        res = []

        while loop:
            y_end = y_start + y_len - sub_len
            for i in range(y_start, y_end):
                res.append(matrix[x_start][i])

            x_end = x_start + x_len - sub_len
            for i in range(x_start, x_end):
                res.append(matrix[i][y_end])

            for i in range(y_end, y_start, -1):
                res.append(matrix[x_end][i])

            for i in range(x_end, x_start, -1):
                res.append(matrix[i][y_start])

            x_start += 1
            y_start += 1
            sub_len += 2
            loop -= 1

        if n % 2:
            if x_len > y_len:
                for i in range(mid, mid + x_len - y_len + 1):
                    res.append(matrix[i][mid])
            else:
                for i in range(mid, mid + y_len - x_len + 1):
                    res.append(matrix[mid][i])
        return res
# leetcode submit region end(Prohibit modification and deletion)
