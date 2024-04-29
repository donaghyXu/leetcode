# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 10⁹ + 7 取模。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit 
# 
#  示例 2： 
# 
#  
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 1000 
#  s 和 t 由英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 1230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 动态规划
        # 时间复杂度：O(s_len * t_len)
        # 空间复杂度：O(s_len * t_len)

        s_len = len(s)
        t_len = len(t)
        # dp[i][j]：以i-1下标的s子序列中出现到j-1下标的序列的个数
        dp = [[0 for _ in range(t_len + 1)] for _ in range(s_len + 1)]

        # 初始化
        for i in range(s_len):
            dp[i][0] = 1

        # 递推 遍历
        for i in range(1, s_len + 1):
            for j in range(1, t_len + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[s_len][t_len]
# leetcode submit region end(Prohibit modification and deletion)
