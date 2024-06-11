# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 10108 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2.滑动窗口，哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        hash_dict = {}
        max_length = 0
        n = len(s)
        left = 0
        right = 0
        while right < n:
            # 扩大窗口
            if s[right] not in hash_dict:
                hash_dict[s[right]] = 1
            else:
                # 判断结果
                max_length = max(max_length, right - left)
                # 缩小窗口
                while s[left] != s[right]:
                    hash_dict.pop(s[left])
                    left += 1
                left += 1
            right += 1

            # 剪枝
            if max_length > n - left:
                break
        max_length = max(max_length, right - left)
        return max_length

        # 1.暴力破解
        # 时间复杂度：O(n³)，双重for循环查找所有子串O(n²)，判断是否有不重复子串O(n)
        # 空间复杂度：O(n)
# leetcode submit region end(Prohibit modification and deletion)
