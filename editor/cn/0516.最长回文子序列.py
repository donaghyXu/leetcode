# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。 
# 
#  子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 1202 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 动态规划
        # 时间复杂度：O(s_len * s_len)
        # 空间复杂度：O(s_len * s_len)

        s_len = len(s)

        # dp[i][j]：坐标在[i, j]范围内的最长回文子序列长度
        dp = [[0 for _ in range(s_len)] for _ in range(s_len)]

        # 初始化
        for i in range(s_len):
            dp[i][i] = 1

        # 递推，遍历
        for i in range(s_len - 1, -1, -1):
            for j in range(i + 1, s_len):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][s_len - 1]
# leetcode submit region end(Prohibit modification and deletion)
