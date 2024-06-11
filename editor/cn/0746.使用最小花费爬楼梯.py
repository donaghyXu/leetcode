# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。 
# 
#  你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。 
# 
#  请你计算并返回达到楼梯顶部的最低花费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：你将从下标为 0 的台阶开始。
# - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
# - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
# - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
# 总花费为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
# 
#  Related Topics 数组 动态规划 👍 1474 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 2.动态规划优化空间复杂度
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        n = len(cost)
        # 定义dp[i]为到第i个阶梯所需花费的最小体力
        dp = [0] * 2

        # 初始化
        dp[0] = 0
        dp[1] = 0

        # 递推，遍历
        for i in range(2, n + 1):
            min_value = min(dp[1] + cost[i - 1], dp[0] + cost[i - 2])
            dp[0] = dp[1]
            dp[1] = min_value
        return dp[1]

        # # 1.动态规划
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        #
        # n = len(cost)
        # # 定义dp[i]为到第i个阶梯所需花费的最小体力
        # dp = [0] * (n+1)
        #
        # # 初始化
        # dp[0] = 0
        # dp[1] = 0
        #
        # # 递推，遍历
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
