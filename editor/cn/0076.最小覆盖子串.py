# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  m == s.length 
#  n == t.length 
#  1 <= m, n <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 
# o(m+n) 时间内解决此问题的算法吗？
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 2884 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        # 时间复杂度：O(s_len*t_len)
        # 空间复杂度：O(s_len+t_len)

        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return ""

        # 计算各字符出现的数量
        t_dict = collections.defaultdict(int)
        for element in t:
            t_dict[element] += 1

        result = ""
        min_len = s_len + 1

        left = 0
        right = 0
        while right < s_len:
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
            # 符合滑动窗口的要求，计算子串
            while self.is_contain(t_dict) and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                # 滑动窗口收缩
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                left += 1
            # 滑动窗口扩展
            right += 1
        return result

    # 判断子串是否被覆盖
    def is_contain(self, hash_dict):
        for key, value in hash_dict.items():
            if value > 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
