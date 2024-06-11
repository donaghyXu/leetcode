# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。 请你实现时间复杂度为 
# O(n) 并且只使用常数级别额外空间的解决方案。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  Related Topics 数组 哈希表 👍 2136 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：没有出现的最小正整数必然在[1,n]之间
        #      不断地将正整数nums[i]放回下标nums[i]-1处
        #      如果 nums[i]恰好与nums[nums[i] - 1]相等，
        #      说明 nums[i]已经出现在了正确的位置。因此我们可以跳出循环，开始遍历下一个数
        #      最后遍历一遍，如果下标i位置上的不是i+1，那么该数没有出现

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                idx = nums[i]
                nums[i], nums[idx - 1] = nums[idx - 1], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
# leetcode submit region end(Prohibit modification and deletion)
