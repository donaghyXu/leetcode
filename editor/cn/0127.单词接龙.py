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
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 广搜
        # 时间复杂度：O(mn) n=len(beginWord), m=len(wordList)
        # 空间复杂度：O(m)
        if endWord not in wordList or len(wordList) == 0:
            return 0

        word_set = set(wordList)

        queue = collections.deque()
        queue.append(beginWord)
        cnt_map = {beginWord: 1}

        while queue:
            word = queue.popleft()
            cnt = cnt_map[word]
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    word_join = ''.join(word_list)
                    if word_join == endWord:
                        return cnt + 1
                    if word_join not in cnt_map and word_join in word_set:
                        cnt_map[word_join] = cnt + 1
                        queue.append(word_join)
        return 0
# leetcode submit region end(Prohibit modification and deletion)
