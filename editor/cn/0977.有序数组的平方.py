# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
# 
#  Related Topics 数组 双指针 排序 👍 983 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # 暴力解法 o(n) + o(nlogn)
        # for i in range(len(nums)):
        #     nums[i] **= 2
        # nums.sort()
        # return nums

        # 双指针 o(n)
        res = [None] * len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res[index] = nums[left] ** 2
                left += 1
            else:
                res[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
