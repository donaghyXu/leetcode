# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。 
# 
#  数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 15 
#  -100 <= nums[i] <= 100 
#  
# 
#  Related Topics 位运算 数组 哈希表 回溯 👍 781 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        # 时间复杂度：O(n * 2^n)
        # 空间复杂度：O(n)
        self.back_tracking(nums, 0)
        return self.result

    def back_tracking(self, nums, start_index):
        if len(self.path) >= 2:
            self.result.append(self.path[:])

        level_set = set()
        for i in range(start_index, len(nums)):
            # 同一树层去重
            if nums[i] not in level_set:
                # 如果满足递增，进入下一层回溯
                if len(self.path) == 0 or \
                        (len(self.path) > 0 and nums[i] >= self.path[-1]):
                    level_set.add(nums[i])
                    self.path.append(nums[i])
                    self.back_tracking(nums, i + 1)
                    self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
