# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: numRows = 1
# 输出: [[1]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics 数组 动态规划 👍 1166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 动态规划
        # 时间复杂度：O(n)，n=(numRows²+numRows)/2
        # 空间复杂度：O(n)

        result = []
        for row in range(numRows):
            row_list = [1 for _ in range(row + 1)]
            result.append(row_list)

        # 递推，遍历
        for row in range(2, numRows):
            for col in range(1, row):
                result[row][col] = result[row - 1][col - 1] + result[row - 1][col]
        return result
# leetcode submit region end(Prohibit modification and deletion)
