# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  
# 
#  Related Topics 广度优先搜索 数学 动态规划 👍 1954 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 动态规划
        # 时间复杂度：O(sqrt(n) * n)
        # 空间复杂度：O(n)

        # dp[i]：和为i的完全平方数的最少数量
        dp = [10005 for _ in range(n + 1)]

        # 初始化
        dp[0] = 0

        # 递推，遍历，先物品后背包，完全背包
        target = int(math.sqrt(n))
        for i in range(1, target + 1):
            for j in range(i ** 2, n + 1):
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
