# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。 
# 
#  题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。 
# 
#  请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内 
#  
# 
#  
# 
#  进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。） 
# 
#  Related Topics 数组 前缀和 👍 1793 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2.前缀和优化版
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        left = [1 for _ in range(n)]
        r = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 1, -1, -1):
            left[i] = left[i] * r
            r = r * nums[i]
        return left

        # # 1. 前缀和
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # n = len(nums)
        # left = [1 for _ in range(n)]
        # right = [1 for _ in range(n)]
        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        # for i in range(n-2, -1, -1):
        #     right[i] = right[i+1] * nums[i+1]
        # return [left[i] * right[i] for i in range(n)]
# leetcode submit region end(Prohibit modification and deletion)
