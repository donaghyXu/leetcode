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
        # 4.哈希表和滑动窗口，直接从重复字符后一个开始滑动，时间复杂度O(n)
        # 法一
        m = 0
        index = [0] * 128
        start = 0
        for i in range(len(s)):
            if index[ord(s[i])] > start:  # 判断字符是否重复
                count = i - start
                if count > m:
                    m = count
                start = index[ord(s[i])]
            index[ord(s[i])] = i + 1
        count = len(s) - start
        return count if count > m else m

        # m = 0
        # index = [0] * 128
        # start = 0
        # for i, c in enumerate(s):
        #     if index[ord(c)] > start: # 判断字符是否重复
        #         count = i - start
        #         if count > m:
        #             m = count
        #         start = index[ord(c)]
        #     index[ord(c)] = i + 1
        # count = len(s) - start
        # return count if count > m else m

        # 3.哈希表和滑动窗口，时间复杂度O(n)
        # # 哈希集合，记录每个字符是否出现过
        # occ = set()
        # n = len(s)
        # # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        # rk = -1
        # res = 0
        # for i in range(n):
        #     # 扩大窗口
        #     while (rk + 1) < n and s[rk + 1] not in occ:
        #         occ.add(s[rk + 1])
        #         rk += 1
        #     # 缩小窗口
        #     if (rk + 1) < n and s[rk + 1] in occ:
        #         occ.remove(s[i])
        #     res = max(res, rk - i + 1)
        #     # if res > (n - i - 1):
        #     #     break
        # return res

        # 2.滑动窗口，查找子串，时间复杂度O(n²)
        # max_cnt = 0
        # i = 0
        # n = len(s)
        # while(i < n):
        #     cnt = 1
        #     for j in range(i+1, n):
        #         if s[j] not in s[i:j]:  # 切片时间复杂度过高
        #             cnt += 1
        #             continue
        #         else:
        #             i = i + s[i:j].find(s[j]) + 1
        #             break
        #     if cnt > max_cnt:
        #         max_cnt = cnt
        #     if max_cnt > len(s[(i+1):]):
        #         break
        # return max_cnt

        # 1.暴力破解，双重for循环查找所有子串O(n²)，判断是否有不重复子串O(n)，总体时间复杂度O(n³)，空间复杂度O(m)
# leetcode submit region end(Prohibit modification and deletion)
