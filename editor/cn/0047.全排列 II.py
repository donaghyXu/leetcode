# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 数组 回溯 👍 1563 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n!*n)
        # 空间复杂度：O(n)
        nums.sort()
        used = [False] * len(nums)
        self.back_tracking(nums, used)
        return self.result

    def back_tracking(self, nums, used):
        # 终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return

        level_set = set()
        for i in range(len(nums)):
            # 同一树层去重，树枝去重(取过的数不再取)
            if nums[i] in level_set or used[i]:
                continue
            level_set.add(nums[i])
            self.path.append(nums[i])
            used[i] = True
            self.back_tracking(nums, used)
            used[i] = False
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
