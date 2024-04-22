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
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for element in t:
            if element in t_dict:
                t_dict[element] += 1
            else:
                t_dict[element] = 1

        left = 0
        right = 0
        res_dict = {}
        res_sub_str = ''
        min_len = float('inf')
        while right < len(s):
            if s[right] in res_dict:
                res_dict[s[right]] += 1
            else:
                res_dict[s[right]] = 1
            flag = True
            for key, value in t_dict.items():
                if key not in res_dict:
                    flag = False
                    break
                if key in res_dict and value > res_dict[key]:
                    flag = False
                    break
            while flag:
                sub_len = right - left + 1
                if sub_len < min_len:
                    min_len = sub_len
                    res_sub_str = s[left:right + 1]

                res_dict[s[left]] -= 1
                left += 1
                for key, value in t_dict.items():
                    if key not in res_dict:
                        flag = False
                        break
                    if key in res_dict and value > res_dict[key]:
                        flag = False
                        break
            right += 1
        return res_sub_str
# leetcode submit region end(Prohibit modification and deletion)
