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
        # 双指针法 + min_max剪枝
        # 时间复杂度: O(n³)
        # 空间复杂度: O(1)
        # 思路：通过双指针将四层for循环降为三层，固定前两个数，另外两个数通过双指针查找

        res = []
        n = len(nums)
        if n < 4:
            return res
        nums.sort()

        # min_max剪枝，最小值比目标值还大，最大值比目标值还小，都不可能找到符合目标值的结果
        min_value = nums[0] + nums[1] + nums[2] + nums[3]
        max_value = nums[-1] + nums[-2] + nums[-3] + nums[-4]
        if min_value > target or max_value < target:
            return res

        for i in range(n - 3):
            # 剪枝，第一个数相同的情况
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, n - 2):
                # 剪枝，第二个数相同的情况
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # min_max剪枝，最小值比目标值还大，最大值比目标值还小，都不可能找到符合目标值的结果
                min_value = nums[i] + nums[j] + nums[j+1] + nums[j+2]
                max_value = nums[i] + nums[j] + nums[-1] + nums[-2]
                if min_value > target or max_value < target:
                    continue

                left = j + 1
                right = n - 1
                target_new = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == target_new:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # 剪枝，去除第三个数重复的情况
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 剪枝，去除第四个数重复的情况
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target_new:
                        left += 1
                    else:
                        right -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
