# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1 ： 
# 
#  
# 输入：nums = [2,2,1]
# 输出：1
#  
# 
#  示例 2 ： 
# 
#  
# 输入：nums = [4,1,2,1,2]
# 输出：4
#  
# 
#  示例 3 ： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  除了某个元素只出现一次以外，其余每个元素均出现两次。 
#  
# 
#  Related Topics 位运算 数组 👍 3155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：异或运算的三条性质
        #      1.任何数和0做异或运算，结果仍然是原来的数
        #      2.任何数和自身做异或运算，结果为0
        #      3.异或满足交换律
        #      所以，a ^ b ^ a = a ^ a ^ b = b

        result = 0
        for num in nums:
            result ^= num
        return result
# leetcode submit region end(Prohibit modification and deletion)
