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
        # 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n_list = list(str(n))
        n_len = len(n_list)
        flag = n_len
        for i in range(n_len - 1, 0, -1):
            if n_list[i] < n_list[i - 1]:
                n_list[i] = str(9)
                n_list[i - 1] = str(int(n_list[i - 1]) - 1)
                flag = i
        for i in range(flag, n_len):
            n_list[i] = str(9)
        return int("".join(n_list))
# leetcode submit region end(Prohibit modification and deletion)
