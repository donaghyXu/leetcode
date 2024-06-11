# 给定一个包含红色、白色和蓝色、共 n 个元素的数组
#  nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。 
# 
#  我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。 
# 
#  
#  
# 
#  必须在不使用库内置的 sort 函数的情况下解决这个问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  nums[i] 为 0、1 或 2 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能想出一个仅使用常数空间的一趟扫描算法吗？ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1783 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针，技巧
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：将0置换到前面，将2置换到后面

        n = len(nums)
        left = 0
        right = n - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            # 置换到当前位置的可能为0或2，就继续循环判断当前位置，当为1的时候，指针挪到下一个位置
            else:
                i += 1
# leetcode submit region end(Prohibit modification and deletion)
