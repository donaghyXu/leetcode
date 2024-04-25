# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 2059 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 动态规划
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n)
        n = len(nums)
        total_value = sum(nums)
        if total_value % 2:
            return False
        target = int(total_value / 2)

        # dp[j] 0-i的数放进容量为j的背包的最大总和
        # j的最大值为target
        dp = [0] * (target + 1)

        # 递推，遍历
        for i in range(n):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
            if dp[target] == target:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
