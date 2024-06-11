# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
# 
#  Related Topics 栈 字符串 动态规划 👍 2515 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        n = len(s)
        if n <= 1:
            return 0

        # dp[i]:以下标i结尾的最长有效括号子串的长度
        dp = [0 for _ in range(n)]

        # 初始化
        if s[0] == "(" and s[1] == ")":
            dp[1] = 2

        max_len = dp[1]
        # 递推，遍历
        for i in range(2, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
            max_len = max(max_len, dp[i])
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
