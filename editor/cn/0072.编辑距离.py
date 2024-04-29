# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 3374 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 动态规划
        # 时间复杂度：O(word1_len * word2_len)
        # 空间复杂度：O(word1_len * word2_len)

        word1_len = len(word1)
        word2_len = len(word2)

        # dp[i][j]：到下标i-1的word1子串 和 到下标j-1的word2子串 一样的最少操作次数
        dp = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]

        # 初始化
        for i in range(word1_len + 1):
            dp[i][0] = i
        for j in range(1, word2_len + 1):
            dp[0][j] = j

        # 递推 遍历
        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 删，删，换    增加操作数等同于删
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[word1_len][word2_len]
# leetcode submit region end(Prohibit modification and deletion)
