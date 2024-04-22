# 给定一个二维数组 array，请返回「螺旋遍历」该数组的结果。 
# 
#  螺旋遍历：从左上角开始，按照 向右、向下、向左、向上 的顺序 依次 提取元素，然后再进入内部一层重复相同的步骤，直到提取完所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：array = [[1,2,3],[8,9,4],[7,6,5]]
# 输出：[1,2,3,4,5,6,7,8,9]
#  
# 
#  示例 2： 
# 
#  
# 输入：array  = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
# 输出：[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= array.length <= 100 
#  0 <= array[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
# 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 602 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        n_x = len(array)
        if n_x == 0:
            return []
        n_y = len(array[0])

        n = min(n_x, n_y)
        loop = int(n / 2)
        x_start = 0
        y_start = 0
        offset = 1
        res = []

        while loop:
            y_end = y_start + n_y - offset
            for i in range(y_start, y_end):
                res.append(array[x_start][i])

            x_end = x_start + n_x - offset
            for i in range(x_start, x_end):
                res.append(array[i][y_end])

            for i in range(y_end, y_start, -1):
                res.append(array[x_end][i])

            for i in range(x_end, x_start, -1):
                res.append(array[i][y_start])

            x_start += 1
            y_start += 1
            loop -= 1
            offset += 2

        mid = int(n / 2)
        if n % 2 == 1:
            if n_x > n_y:
                for i in range(mid, mid + n_x - n_y + 1):
                    res.append(array[i][mid])
            else:
                for i in range(mid, mid + n_y - n_x + 1):
                    res.append(array[mid][i])
        return res
# leetcode submit region end(Prohibit modification and deletion)
