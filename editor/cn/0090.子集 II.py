# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 1205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)

        # 去重需要排序
        nums.sort()
        self.result.append([])
        self.back_tracking(nums, 0)
        return self.result

    def back_tracking(self, nums, start_index):
        # 终止条件
        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            # 同树层去重
            if i > start_index and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.result.append(self.path[:])
            self.back_tracking(nums, i + 1)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
