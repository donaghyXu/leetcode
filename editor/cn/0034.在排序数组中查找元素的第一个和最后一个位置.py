# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 👍 2674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        # 查找第一个大于等于target的位置
        left = self.left_binary_search(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = self.left_binary_search(nums, target + 1) - 1
        return [left, right]

    # 第一个大于等于target的地方
    def left_binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
# leetcode submit region end(Prohibit modification and deletion)
