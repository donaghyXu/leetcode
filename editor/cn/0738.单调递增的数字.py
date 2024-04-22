# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。 
# 
#  给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  
# 输入: n = 332
# 输出: 299
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics 贪心 数学 👍 463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n_list = list(str(n))
        start = len(n_list) - 1
        flag = len(n_list)
        while start >= 1:
            if int(n_list[start - 1]) > int(n_list[start]):
                flag = start
                n_list[start - 1] = int(n_list[start - 1]) - 1
            start -= 1
        for i in range(len(n_list)):
            if i >= flag:
                n_list[i] = '9'
            else:
                n_list[i] = str(n_list[i])
        return int("".join(n_list))
# leetcode submit region end(Prohibit modification and deletion)
