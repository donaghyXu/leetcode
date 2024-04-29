# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics 双指针 字符串 动态规划 👍 7186 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        # 时间复杂度：O(s_len * s_len)
        # 空间复杂度：O(s_len * s_len)

        s_len = len(s)
        result = ""

        # dp[i][j]：下标在[i,j]范围内的子串是否是回文子串
        dp = [[False for _ in range(s_len)] for _ in range(s_len)]

        # 递推 遍历
        for i in range(s_len - 1, -1, -1):
            for j in range(i, s_len):
                if s[i] == s[j]:
                    if (j - i) <= 1 or ((j - i) > 1 and dp[i+1][j-1]):
                        dp[i][j] = True
                        if len(s[i:j+1]) > len(result):
                            result = s[i:j+1]
        return result
# leetcode submit region end(Prohibit modification and deletion)
