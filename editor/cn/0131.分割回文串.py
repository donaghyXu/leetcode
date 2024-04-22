# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 1772 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：
        self.back_tracking(s, 0)
        return self.result

    def is_palindrome(self, s: str):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def back_tracking(self, s, start_index):
        # 终止条件
        if start_index >= len(s):
            self.result.append(self.path[:])
            return

        start = start_index
        for i in range(start_index, len(s)):
            part = s[start:i+1]
            if self.is_palindrome(part):
                self.path.append(part)
                self.back_tracking(s, i + 1)
                self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
