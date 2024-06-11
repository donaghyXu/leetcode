# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件： 
# 
#  
#  只使用数字1到9 
#  每个数字 最多使用一次 
#  
# 
#  返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。 
# 
#  示例 2: 
# 
#  
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。 
# 
#  示例 3: 
# 
#  
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
#  
# 
#  
# 
#  提示: 
# 
#  
#  2 <= k <= 9 
#  1 <= n <= 60 
#  
# 
#  Related Topics 数组 回溯 👍 836 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)
        self.back_tracking(1, k, n)
        return self.result

    def back_tracking(self, start_index, k, n):
        # 终止条件
        if len(self.path) == k and sum(self.path) == n:
            self.result.append(self.path[:])
            return
        if sum(self.path) > n:
            return

        for i in range(start_index, 10 - (k - len(self.path)) + 1):
            self.path.append(i)
            self.back_tracking(i+1, k, n)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
