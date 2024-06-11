# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而
# "aec"不是）。 
# 
#  进阶： 
# 
#  如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代
# 码？ 
# 
#  致谢： 
# 
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10^4 
#  两个字符串都只由小写字符组成。 
#  
# 
#  Related Topics 双指针 字符串 动态规划 👍 1036 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2.动态规划
        # 时间复杂度：O(s_len*t_len)
        # 空间复杂度：O(s_len*t_len)

        s_len = len(s)
        t_len = len(t)
        if s_len > t_len:
            return False
        if s_len == 0:
            return True

        # dp[i][j]:到位置i-1的子序列和到位置j-1的子序列相等的长度
        dp = [[0 for _ in range(t_len+1)] for _ in range(s_len+1)]

        for i in range(1, s_len + 1):
            for j in range(1, t_len + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]
                if dp[i][j] == s_len:
                    return True
        return False

        # # 1.双指针
        # # 时间复杂度：O(s_len+t_len)
        # # 空间复杂度：O(1)
        # s_index = 0
        # t_index = 0
        # s_len = len(s)
        # t_len = len(t)
        # if s_len > t_len:
        #     return False
        # while s_index < s_len and t_index < t_len:
        #     if t[t_index] == s[s_index]:
        #         s_index += 1
        #     t_index += 1
        # if s_index == s_len:
        #     return True
        # else:
        #     return False
# leetcode submit region end(Prohibit modification and deletion)
