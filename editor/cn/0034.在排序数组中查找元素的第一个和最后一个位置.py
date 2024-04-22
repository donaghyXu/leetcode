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
        # flag = -1
        # start = 0
        # end = len(nums) - 1
        # while start <= end:
        #     mid = start + (end - start) // 2
        #     if nums[mid] > target:
        #         end = mid - 1
        #     elif nums[mid] < target:
        #         start = mid + 1
        #     else:
        #         flag = mid
        #         break
        # if flag == -1:
        #     return [-1, -1]
        # else:
        #     index = flag
        #     min_index = index
        #     max_index = index
        #     while min_index >= 0 and nums[min_index] == nums[index]:
        #         min_index -= 1
        #     while max_index <= end and nums[max_index] == nums[index]:
        #         max_index += 1
        #     return [min_index+1, max_index-1]

        n = len(nums)
        left_index = self.binary_search_find_left(nums, target)
        if left_index >= n or nums[left_index] != target:
            return [-1, -1]
        right_index = self.binary_search_find_right(nums, target)
        return [left_index, right_index]

    def binary_search_find_left(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def binary_search_find_right(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return end

# leetcode submit region end(Prohibit modification and deletion)
