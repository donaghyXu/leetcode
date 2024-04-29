# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。 
# 
#  回文字符串 是正着读和倒过来读一样的字符串。 
# 
#  子字符串 是字符串中的由连续字符组成的一个序列。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 双指针 字符串 动态规划 👍 1321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划
        # 时间复杂度：O(s_len * s_len)
        # 空间复杂度：O(s_len * s_len)

        s_len = len(s)
        result = 0

        # dp[i][j]：区间范围[i,j]的子串是否是回文子串
        dp = [[False for _ in range(s_len)] for _ in range(s_len)]

        # 递推 遍历
        for i in range(s_len - 1, -1, -1):
            for j in range(i, s_len):
                if s[i] == s[j]:
                    if (j - i) <= 1:
                        result += 1
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            result += 1
                            dp[i][j] = True
        return result

    # def countSubstrings(self, s: str) -> int:
    #     # 双指针
    #     # 时间复杂度：O(s_len * s_len)
    #     # 空间复杂度：O(1)
    #     result = 0
    #     for i in range(len(s)):
    #         result += self.extend(s, i, i)
    #         result += self.extend(s, i, i + 1)
    #     return result
    #
    # def extend(self, s, i, j):
    #     s_len = len(s)
    #     result = 0
    #     while i >= 0 and j < s_len and s[i] == s[j]:
    #         result += 1
    #         i -= 1
    #         j += 1
    #     return result
# leetcode submit region end(Prohibit modification and deletion)

