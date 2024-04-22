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
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        matrix = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0
        loop = int(n / 2)
        middle = int(n / 2)
        offset = 1
        cnt = 1

        while loop:

            for j in range(start_y, start_y + n - offset):
                matrix[start_x][j] = cnt
                cnt += 1

            y_end = start_y + n - offset
            for i in range(start_x, start_x + n - offset):
                matrix[i][y_end] = cnt
                cnt += 1

            x_end = start_x + n - offset
            for j in range(y_end, start_y, -1):
                matrix[x_end][j] = cnt
                cnt += 1

            y_end = start_y
            for i in range(x_end, start_x, -1):
                matrix[i][y_end] = cnt
                cnt += 1

            start_x += 1
            start_y += 1
            loop -= 1
            offset += 2

        if n % 2:
            matrix[middle][middle] = cnt
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
