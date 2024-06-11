# 给定一个非空的字符串
#  s ，检查是否可以通过由它的一个子串重复多次构成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aba"
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 字符串匹配 👍 1160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def get_next(self, s: str):
        i = 0
        next = [0] * len(s)
        next[0] = i
        for j in range(1, len(s)):
            while i >= 1 and s[i] != s[j]:
                i = next[i-1]
            if s[i] == s[j]:
                i += 1
            next[j] = i
        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        # 2. KMP
        # 时间复杂度：O(n+m)
        # 空间复杂度：O(n)
        if len(s) == 0:
            return False
        next = self.get_next(s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False

    # def repeatedSubstringPattern(self, s: str) -> bool:
    #     # 1. 移动匹配
    #     # 时间复杂度：O(n)
    #     # 空间复杂度：O(1)
    #     t = s + s
    #     t = t[1:-1]
    #     if t.find(s) != -1:
    #         return True
    #     return False
# leetcode submit region end(Prohibit modification and deletion)
