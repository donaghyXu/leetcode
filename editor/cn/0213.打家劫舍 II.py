# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的
# 房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 1000 
#  
# 
#  Related Topics 数组 动态规划 👍 1583 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n = len(nums)
        if n <= 3:
            return max(nums)

        # dp[i][j]：第i个房屋所能偷窃到的最高金额
        # dp1：范围是第0个房屋到第n-2个房屋
        # dp2：范围是第1个房屋到第n-1个房屋
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]

        # 初始化
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        # 递推，遍历
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + nums[i + 1], dp2[i - 1])
        return max(dp1[n - 2], dp2[n - 2])
# leetcode submit region end(Prohibit modification and deletion)
