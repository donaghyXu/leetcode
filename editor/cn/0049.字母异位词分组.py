# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。 
# 
#  字母异位词 是由重新排列源单词的所有字母得到的一个新单词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# 
#  示例 2: 
# 
#  
# 输入: strs = [""]
# 输出: [[""]]
#  
# 
#  示例 3: 
# 
#  
# 输入: strs = ["a"]
# 输出: [["a"]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] 仅包含小写字母 
#  
# 
#  Related Topics 数组 哈希表 字符串 排序 👍 1876 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 哈希表
        # 时间复杂度：O(n*klogk)，n=len(strs)，k=max(len(str))
        # 空间复杂度：O(n)
        # 思路：通过哈希表索引字母异位词，将字母异位词排序后作为key
        hash_dict = collections.defaultdict(list)
        for word in strs:
            word_sort = "".join(sorted(word))
            hash_dict[word_sort].append(word)

        return list(hash_dict.values())
# leetcode submit region end(Prohibit modification and deletion)
