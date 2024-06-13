# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 2733 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 2.贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        n = len(nums) - 1
        if nums[0] == 0 and n > 1:
            return False

        start = 0
        # 当前能覆盖的最远范围
        cur_cover = nums[start]
        # 下一次跳跃能覆盖的最远范围
        next_cover = 0

        # 在当前步数可以覆盖的范围内不断更新下一次跳跃能覆盖的最远范围
        while start <= cur_cover:
            if cur_cover >= n:
                return True

            # 更新下一次跳跃能覆盖的最远范围
            next_cover = max(next_cover, start + nums[start])

            if next_cover >= n:
                return True

            # 到达当前能覆盖的最远范围，更新当前能覆盖的最远范围
            if start == cur_cover:
                cur_cover = next_cover

            start += 1
        return cur_cover >= n

        # # 1.动态规划
        # # 时间复杂度：O(n²)
        # # 空间复杂度：O(n)
        #
        # n = len(nums)
        # # dp[i]：是否能到达i位置
        # dp = [False for _ in range(n)]
        #
        # # 初始化
        # dp[0] = True
        #
        # # 递推，遍历
        # for i in range(n):
        #     for j in range(i + 1, i + nums[i] + 1):
        #         if j < n and dp[i]:
        #             if dp[j]:
        #                 continue
        #             else:
        #                 dp[j] = True
        #         if dp[n-1]:
        #             return True
        # return dp[n-1]
# leetcode submit region end(Prohibit modification and deletion)
