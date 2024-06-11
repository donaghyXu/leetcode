# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−2³¹, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  Related Topics 数学 👍 3983 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        # 数学模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        str_x = str(abs(x))
        result = int("".join(list(str_x)[::-1]))
        if x < 0:
            result = -result
        if result >= math.pow(2, 31) or result < -math.pow(2, 31):
            return 0
        return result
# leetcode submit region end(Prohibit modification and deletion)
