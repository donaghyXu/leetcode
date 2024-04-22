# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。 
# 
#  注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。 
# 
#  返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 示例 1：
# 
#  
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
# 
#  示例 2： 
# 
#  
# 输入：s = "eccbbbbdec"
# 输出：[10]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 贪心 哈希表 双指针 字符串 👍 1125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        s_dict = {}
        n = len(s)
        for i in range(n):
            s_dict[s[i]] = i
        right = s_dict[s[0]]
        left = 0
        for i in range(n):
            if i < right and s_dict[s[i]] > right:
                right = s_dict[s[i]]
            if i == right or i == (n - 1):
                res.append(right - left + 1)
                if (i + 1) < n:
                    left = i + 1
                    right = s_dict[s[i + 1]]
        return res
# leetcode submit region end(Prohibit modification and deletion)
