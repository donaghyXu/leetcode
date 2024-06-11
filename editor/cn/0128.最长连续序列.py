# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 并查集 数组 哈希表 👍 2105 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 哈希
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 思路：用哈希表记录元素是否出现过
        #      如果该数的前一个数未出现，那么是一个子序列的开头，开始往后遍历计数
        max_length = 0
        nums_set = set(nums)

        for num in nums_set:
            # 判断是否是连续子序列的开头
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
# leetcode submit region end(Prohibit modification and deletion)
