# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
#  
# 
#  Related Topics 数组 动态规划 👍 2250 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)

        # dp[i]:以下标i结尾的最大乘积,j=0代表最大乘积，j=1代表最小乘积
        dp = [[0, 0] for _ in range(n)]

        # 初始化
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        max_mul = nums[0]
        # 递推，遍历
        for i in range(1, n):
            dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            max_mul = max(max_mul, dp[i][0])

        return max_mul
# leetcode submit region end(Prohibit modification and deletion)
