# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  请注意 ，必须在不复制数组的情况下原地对数组进行操作。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [0]
# 输出: [0] 
# 
#  
# 
#  提示: 
#  
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶：你能尽量减少完成的操作次数吗？ 
# 
#  Related Topics 数组 双指针 👍 2352 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left = 0
        # right = 0
        # while left < len(nums) and right < len(nums):
        #     while left < len(nums) and nums[left] != 0:
        #         left += 1
        #     if left >= len(nums):
        #         break
        #     right = left + 1
        #     while right < len(nums) and nums[right] == 0:
        #         right += 1
        #     if right < len(nums):
        #         nums[left] = nums[right]
        #         nums[right] = 0
        #         left += 1
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
# leetcode submit region end(Prohibit modification and deletion)
