# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
#  nums 中的所有元素 互不相同 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 2281 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)
        self.result.append([])
        self.back_tracking(nums, 0)
        return self.result

    def back_tracking(self, nums, start_index):
        # 终止条件
        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.result.append(self.path[:])
            self.back_tracking(nums, i + 1)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
