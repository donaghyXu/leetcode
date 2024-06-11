# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。 
# 
#  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。 
# 
#  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2： 
# 
#  
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 动态规划 👍 3480 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3.动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n = len(prices)
        # dp[i][j]:第i+1天手中持有的最大现金，j=0代表持有股票，j=1代表不持有
        dp = [[0, 0] for _ in range(n)]

        # 初始化
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        # 递推，遍历
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[n-1][1]

        # # 2.贪心
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # low = 10005
        # high = -1
        # for i in range(len(prices)):
        #     low = min(low, prices[i])
        #     high = max(high, prices[i] - low)
        # return high

        # # 1.简单模拟 超时
        # # 时间复杂度：O(n²)
        # # 空间复杂度：O(1)
        #
        # res = 0
        # for i in range(len(prices)-1):
        #     last_max = max(prices[i+1:])
        #     res = max(res, last_max - prices[i])
        # return res
# leetcode submit region end(Prohibit modification and deletion)
