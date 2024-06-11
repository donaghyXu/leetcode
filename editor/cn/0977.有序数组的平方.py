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
        # 2.双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        index = n - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return result

        # # 1.暴力解法
        # # 时间复杂度：O(nlogn)
        # # 空间复杂度：O(1)
        # for i in range(len(nums)):
        #     nums[i] **= 2
        # nums.sort()
        # return nums
# leetcode submit region end(Prohibit modification and deletion)
