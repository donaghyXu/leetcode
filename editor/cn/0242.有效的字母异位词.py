# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  Related Topics 哈希表 字符串 排序 👍 915 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # count
        # if len(s) != len(t):
        #     return False
        # s_count = Counter()
        # t_count = Counter()
        # for i in range(len(s)):
        #     s_count[s[i]] += 1
        #     t_count[t[i]] += 1
        # if s_count == t_count:
        #     return True
        # else:
        #     return False

        # 数组
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for element in s:
            cnt[ord(element) - ord('a')] += 1
        for element in t:
            cnt[ord(element) - ord('a')] -= 1
        for i in range(26):
            if cnt[i] != 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
