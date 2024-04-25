# 给你一个非负整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
# 
#  Related Topics 数组 动态规划 回溯 👍 1901 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 动态规划
        # 时间复杂度：O(n * target_new)
        # 空间复杂度：O(target_new)

        n = len(nums)
        total = sum(nums)
        target_new = int((total + target) / 2)
        if (total + target) % 2 or abs(target) > total:
            return 0
        target_new = int(target_new)

        # dp[j]：构成j，有dp[j]种方法
        dp = [0] * (target_new + 1)

        # 初始化
        dp[0] = 1

        # 递归 遍历
        # left + right = sum  left - right = target  left=(sum+target)/2
        for i in range(n):
            for j in range(target_new, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[target_new]
# leetcode submit region end(Prohibit modification and deletion)
