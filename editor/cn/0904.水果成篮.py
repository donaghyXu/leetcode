# 你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。 
# 
#  你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果： 
# 
#  
#  你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。 
#  你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到
# 下一棵树，并继续采摘。 
#  一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。 
#  
# 
#  给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：fruits = [1,2,1]
# 输出：3
# 解释：可以采摘全部 3 棵树。
#  
# 
#  示例 2： 
# 
#  
# 输入：fruits = [0,1,2,2]
# 输出：3
# 解释：可以采摘 [1,2,2] 这三棵树。
# 如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。
#  
# 
#  示例 3： 
# 
#  
# 输入：fruits = [1,2,3,2,2]
# 输出：4
# 解释：可以采摘 [2,3,2,2] 这四棵树。
# 如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。
#  
# 
#  示例 4： 
# 
#  
# 输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
# 输出：5
# 解释：可以采摘 [1,2,1,1,2] 这五棵树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= fruits.length <= 10⁵ 
#  0 <= fruits[i] < fruits.length 
#  
# 
#  Related Topics 数组 哈希表 滑动窗口 👍 636 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2.滑动窗口优化版
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        n = len(fruits)
        count = Counter()
        max_result = 0
        start = 0
        end = 0
        while end < n:
            count[fruits[end]] += 1
            # 计算符合水果限制的最大水果数量
            if len(count) <= 2:
                max_result = max(max_result, end - start + 1)
            # 超出水果限制，窗口收缩
            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    count.pop(fruits[start])
                start += 1
            # 窗口扩张
            end += 1
        return max_result

        # # 1.滑动窗口自己实现方法1
        # max_total = 0
        # left = 0
        # right = 0
        # fruit_list = []
        # fruit_dict = {}
        # while right < len(fruits):
        #     fruit = fruits[right]
        #     if fruit not in fruit_list:
        #         fruit_list.append(fruit)
        #     if fruit not in fruit_dict:
        #         fruit_dict[fruit] = 1
        #     else:
        #         fruit_dict[fruit] += 1
        #     if len(fruit_list) > 2:
        #         while fruit_dict[fruit_list[0]] > 0 and fruit_dict[fruit_list[1]] > 0:
        #             fruit_dict[fruits[left]] -= 1
        #             left += 1
        #         if fruit_dict[fruit_list[0]] == 0:
        #             fruit_list.pop(0)
        #         else:
        #             fruit_list.pop(1)
        #     else:
        #         max_total = max(max_total, right-left+1)
        #     right += 1
        # return max_total
# leetcode submit region end(Prohibit modification and deletion)
