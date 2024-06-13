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
        # 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        # 记录字母出现的最后的位置
        n = len(s)
        hash_dict = {}
        for i, element in enumerate(s):
            hash_dict[element] = i

        prev = 0
        start = 0
        # 当前字母所能覆盖的最远范围
        cur_cover = hash_dict[s[start]]
        result = []
        while start <= cur_cover:
            # 只要当前范围内的字母所能达到的范围比现有范围大，就更新现有范围
            if hash_dict[s[start]] > cur_cover:
                cur_cover = hash_dict[s[start]]
            # 开始新的范围
            if start == cur_cover and start + 1 < n:
                result.append(cur_cover - prev + 1)
                prev = start + 1
                cur_cover = hash_dict[s[start + 1]]
            start += 1
        result.append(cur_cover - prev + 1)
        return result
# leetcode submit region end(Prohibit modification and deletion)
