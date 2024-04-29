# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。 
# 
#  在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。 
# 
#  返回 你能获得的 最大 利润 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：prices = [7,1,5,3,6,4]
# 输出：7
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
#      总利润为 4 + 3 = 7 。 
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
#      总利润为 4 。 
# 
#  示例 3： 
# 
#  
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 10⁴ 
#  0 <= prices[i] <= 10⁴ 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 2469 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n = len(prices)
        # dp[i][0]第i天持有股票手上所有的最大现金 dp[i][1]第i天不持有股票手上所有的最大现金
        dp = [[0, 0] for _ in range(n)]

        # 初始化
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        # 递推，循环
        for i in range(1, n):
            # 第i天持有股票
            dp[i][0] = max(dp[i - 1][1] - prices[i], dp[i - 1][0])

            # 第i天不持有股票
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[n - 1][1]

        # # 贪心
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # n = len(prices)
        # res_max = 0
        # for i in range(n-1):
        #     if prices[i+1] > prices[i]:
        #         res_max += (prices[i+1] - prices[i])
        # return res_max
# leetcode submit region end(Prohibit modification and deletion)
