# 给定一个含有 n 个正整数的数组和一个正整数 target 。 
# 
#  找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返
# 回其长度。如果不存在符合条件的子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 
#  
# 
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 2124 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口法
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        left = 0
        right = 0
        min_length = float('inf')
        total_sum = 0
        while right < len(nums):
            total_sum += nums[right]
            while total_sum >= target and left <= right:
                min_length = min(min_length, right - left + 1)
                total_sum -= nums[left]
                left += 1
            right += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length
# leetcode submit region end(Prohibit modification and deletion)
