# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
# 如果 needle 不是 haystack 的一部分，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack 和 needle 仅由小写英文字符组成 
#  
# 
#  Related Topics 双指针 字符串 字符串匹配 👍 2209 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def get_next(self, s: str):
        # 4.KMP next数组不减1版本
        i = 0
        next = [None] * len(s)
        next[0] = i
        for j in range(1, len(s)):
            while i >= 1 and s[i] != s[j]:
                i = next[i-1]
            if s[i] == s[j]:
                i += 1
            next[j] = i
        return next

        # # 3.KMP next数组减1版本
        # i = -1
        # next = [None] * len(s)
        # next[0] = i
        # for j in range(1, len(s)):
        #     while i >= 0 and s[j] != s[i+1]:
        #         i = next[i]
        #     if s[j] == s[i+1]:
        #         i += 1
        #     next[j] = i
        # return next

    def strStr(self, haystack: str, needle: str) -> int:
        # 4.KMP next数组不减1版本
        # 时间复杂度：O(len(haystack)+len(needle)
        # 空间复杂度：O(len(needle))
        if len(needle) == 0:
            return 0
        needle_len = len(needle)
        next = self.get_next(needle)
        j = 0
        for i in range(len(haystack)):
            while j >= 1 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == needle_len:
                return i - needle_len + 1
        return -1

        # # 3.KMP next数组减1版本
        # # 时间复杂度：O(len(haystack)+len(needle)
        # # 空间复杂度：O(len(needle))
        # if len(needle) == 0:
        #     return 0
        # needle_len = len(needle)
        # next = self.get_next(needle)
        # j = -1
        # for i in range(len(haystack)):
        #     while j >= 0 and haystack[i] != needle[j+1]:
        #         j = next[j]
        #     if haystack[i] == needle[j+1]:
        #         j += 1
        #     if j == (needle_len - 1):
        #         return i - needle_len + 1
        # return -1

        # # 2.双指针
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # needle_len = len(needle)
        # haystack_len = len(haystack)
        # if haystack_len < needle_len:
        #     return -1
        #
        # left = 0
        # right = needle_len - 1
        # while right < haystack_len:
        #     sub_str = haystack[left:right+1]
        #     if sub_str == needle:
        #         return left
        #     left += 1
        #     right += 1
        # return -1

        # # 1.库函数
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # return haystack.find(needle)
# leetcode submit region end(Prohibit modification and deletion)
