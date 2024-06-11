# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1537 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)
        candidates.sort()
        self.back_tracking(target, candidates, 0)
        return self.result

    def back_tracking(self, target, candidates, start_index):
        # 终止条件
        if sum(self.path) == target:
            self.result.append(self.path[:])
            return
        # 剪枝
        if sum(self.path) > target:
            return

        for i in range(start_index, len(candidates)):
            # 同层剪枝
            if i > start_index and candidates[i] == candidates[i-1]:
                continue

            self.path.append(candidates[i])
            self.back_tracking(target, candidates, i + 1)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
