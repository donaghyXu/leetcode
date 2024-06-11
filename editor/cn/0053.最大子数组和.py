# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
# 
#  Related Topics 数组 分治 动态规划 👍 6639 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 2.动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n = len(nums)
        # dp[i]：以下标i结尾的连续子数组的最大和
        dp = [0 for _ in range(n)]

        # 初始化
        dp[0] = nums[0]
        result = dp[0]

        # 递推，遍历
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result

        # # 1.贪心
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # # 思路：计算子数组和，当总和小于0的时候，对于后面的数来说是负贡献
        # #      因此从下一个新的数开始计算累积和
        #
        # result = -float('inf')
        # total_sum = 0
        # for i in range(len(nums)):
        #     total_sum += nums[i]
        #     result = max(result, total_sum)
        #     if total_sum < 0:
        #         total_sum = 0
        # return result
# leetcode submit region end(Prohibit modification and deletion)
