# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s 和 p 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 1428 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑窗 哈希表
        # 时间复杂度：O(len(p)+len(s))
        # 空间复杂度：O(1)
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        # 统计p中字母出现次数
        p_hash_dict = [0 for _ in range(26)]
        for element in p:
            p_hash_dict[ord(element) - ord('a')] += 1

        left = 0
        right = 0
        result = []
        s_hash_dict = [0 for _ in range(26)]
        while right < s_len:
            s_hash_dict[ord(s[right]) - ord('a')] += 1
            # 长度满足条件后，窗口缩小
            while right - left + 1 == p_len:
                if s_hash_dict == p_hash_dict:
                    result.append(left)
                s_hash_dict[ord(s[left]) - ord('a')] -= 1
                left += 1
            # 滑动窗口扩张
            right += 1
        return result
    # leetcode submit region end(Prohibit modification and deletion)
