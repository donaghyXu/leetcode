# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  Related Topics 回溯 👍 1617 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        # 2.回溯 剪枝优化
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)
        self.back_track(n, k, 1)
        return self.result

    def back_track(self, n, k, start_index):
        # 终止条件
        if len(self.path) == k:
            self.result.append(self.path[:])
            return

        # 剪枝，当剩余数量不足K时，中止
        for i in range(start_index, n + 1 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.back_track(n, k, i + 1)
            self.path.pop()

    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     # 1.回溯
    #     # 时间复杂度：O(n * 2^n)
    #     # 空间复杂度：O(n)
    #     self.back_track(n, k, 1)
    #     return self.result
    #
    # def back_track(self, n, k, start_index):
    #     # 终止条件
    #     if len(self.path) == k:
    #         self.result.append(self.path[:])
    #         return
    #
    #     for i in range(start_index, n+1):
    #         self.path.append(i)
    #         self.back_track(n, k, i + 1)
    #         self.path.pop()

# leetcode submit region end(Prohibit modification and deletion)
