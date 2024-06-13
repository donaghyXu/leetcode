# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。 
# 
#  假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。 
# 
#  你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,4,2,2]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,1,3,4,2]
# 输出：3
#  
# 
#  示例 3 : 
# 
#  
# 输入：nums = [3,3,3,3,3]
# 输出：3
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁵ 
#  nums.length == n + 1 
#  1 <= nums[i] <= n 
#  nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如何证明 nums 中至少存在一个重复的数字? 
#  你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？ 
#  
# 
#  Related Topics 位运算 数组 双指针 二分查找 👍 2408 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 双指针，找到有环的地方
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：因数字在[1,n]范围内，因此数字可以对应其索引，当前index的值代表的是下一跳的位置
        #      因为有重复的数，所以会有两个指针指向同一个位置，所以就是找有环的地方

        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# leetcode submit region end(Prohibit modification and deletion)
