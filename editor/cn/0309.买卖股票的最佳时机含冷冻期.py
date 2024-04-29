# 给定一个整数数组
#  prices，其中第 prices[i] 表示第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
# 
#  示例 2: 
# 
#  
# 输入: prices = [1]
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 5000 
#  0 <= prices[i] <= 1000 
#  
# 
#  Related Topics 数组 动态规划 👍 1720 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n*4)

        n = len(prices)

        # dp[i] 第i天所拥有的钱
        # 0：第i天持有股票，1：第i天保持卖出股票状态 2：第i天卖出股票状态 3:第i天不持有股票冻结
        dp = [[0, 0, 0, 0] for _ in range(n)]

        # 初始化
        dp[0][0] = -prices[0]

        # 递推 遍历
        for i in range(1, n):
            # 第i天持有股票
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i], dp[i - 1][3] - prices[i])

            # 第i天保持卖出股票状态
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])

            # 第i天卖出股票状态
            dp[i][2] = dp[i - 1][0] + prices[i]

            # 第i天不持有股票冻结
            dp[i][3] = dp[i - 1][2]

        return max(dp[n - 1][1], dp[n - 1][2], dp[n - 1][3])

# leetcode submit region end(Prohibit modification and deletion)
