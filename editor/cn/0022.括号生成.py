# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 3596 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        # 回溯
        # 时间复杂度：O(4^n / sqrt(n))
        # 空间复杂度：O(n)
        self.back_tracking(0, 0, n)
        return self.result

    def back_tracking(self, open, close, n):
        if len(self.path[:]) == n * 2:
            self.result.append("".join(self.path[:]))
            return

        if open < n:
            self.path.append("(")
            self.back_tracking(open + 1, close, n)
            self.path.pop()

        if close < open:
            self.path.append(")")
            self.back_tracking(open, close + 1, n)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
