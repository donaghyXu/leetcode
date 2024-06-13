# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 2873 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n!)
        # 空间复杂度：O(n)
        used = [False] * len(nums)
        self.back_tracking(nums, used)
        return self.result

    def back_tracking(self, nums, used):
        # 终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return

        for i in range(len(nums)):
            # 树枝去重，避免排列中取到重复的数
            if used[i]:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.back_tracking(nums, used)
            used[i] = False
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
