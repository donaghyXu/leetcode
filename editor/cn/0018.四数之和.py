# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1907 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 3. 双指针法 + min_max剪枝
        # 时间复杂度: O(n^3)
        # 空间复杂度: O(n)

        res = []
        nums.sort()
        num_len = len(nums)
        if num_len < 4:
            return res

        min_value = nums[0] + nums[1] + nums[2] + nums[3]
        max_value = nums[-1] + nums[-2] + nums[-3] + nums[-4]

        if min_value > target or max_value < target:
            return res

        for i, first in enumerate(nums):
            if i >= num_len - 3:
                break
            # 剪枝条件遗忘,需注意
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, num_len - 2):
                # 剪枝条件遗忘，需注意
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                second = nums[j]
                left = j + 1
                right = num_len - 1
                min_value = first + second + nums[left] + nums[left + 1]
                max_value = first + second + nums[right] + nums[right - 1]
                if min_value > target or max_value < target:
                    continue
                while left < right:
                    three_four_sum = target - first - second
                    if (nums[left] + nums[right]) < three_four_sum:
                        left += 1
                    elif (nums[left] + nums[right]) > three_four_sum:
                        right -= 1
                    else:
                        res.append([first, second, nums[left], nums[right]])
                        # 不判断left和right容易越界
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                        left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
