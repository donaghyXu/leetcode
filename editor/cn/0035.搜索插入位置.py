# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  请必须使用时间复杂度为 O(log n) 的算法。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 为 无重复元素 的 升序 排列数组 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  Related Topics 数组 二分查找 👍 2299 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # left = 0
        # right = n - 1
        # while left <= right:
        #     middle = left + (right - left) // 2
        #     if nums[middle] < target:
        #         left = middle + 1
        #     elif nums[middle] > target:
        #         right = middle - 1
        #     else:
        #         return middle
        # return right + 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return start
# leetcode submit region end(Prohibit modification and deletion)
