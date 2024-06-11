# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列
#  beginWord -> s1 -> s2 -> ... -> sk： 
# 
#  
#  每一对相邻的单词只差一个字母。 
#  
#  对于 1 <= i <= k 时，每个
#  si 都在
#  wordList 中。注意， beginWord 不需要在
#  wordList 中。
#  
#  sk == endWord 
#  
# 
#  给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。 
# 
#  示例 1： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= beginWord.length <= 10 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成 
#  beginWord != endWord 
#  wordList 中的所有字符串 互不相同 
#  
# 
#  Related Topics 广度优先搜索 哈希表 字符串 👍 1361 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 广搜
        # 时间复杂度：O(mn) n=len(beginWord), m=len(wordList)
        # 空间复杂度：O(m)

        queue = collections.deque()
        queue.append([beginWord])
        cnt = 1
        hash_dict = {}
        for word in wordList:
            hash_dict[word] = 1

        # 剪枝
        if endWord not in hash_dict:
            return 0

        while queue:
            word_list = queue.popleft()
            next_queue = []
            cnt += 1
            for i in range(len(word_list)):
                word_len = len(word_list[i])
                for j in range(word_len):
                    word = list(word_list[i])
                    for k in range(26):
                        word[j] = chr(ord('a') + k)
                        str_word = "".join(word)
                        if str_word in hash_dict:
                            if str_word == endWord:
                                return cnt
                            next_queue.append(str_word)
                            hash_dict.pop(str_word)
            if next_queue:
                queue.append(next_queue)
        return 0
# leetcode submit region end(Prohibit modification and deletion)