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
        # 时间复杂度：
        # 空间复杂度：
        nums.sort()
        used = [False] * len(nums)
        self.back_tracking(nums, used)
        return self.result

    def back_tracking(self, nums, used):
        # 终止条件
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return

        cur_level_num = set()              # n叉数的同层去重
        for i in range(len(nums)):
            if nums[i] in cur_level_num:
                continue
            if not used[i]:                # 排列去重逻辑
                used[i] = True
                cur_level_num.add(nums[i])
                self.path.append(nums[i])
                self.back_tracking(nums, used)
                self.path.pop()
                used[i] = False
# leetcode submit region end(Prohibit modification and deletion)
