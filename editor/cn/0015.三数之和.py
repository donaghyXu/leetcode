# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != 
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请 
# 
#  你返回所有和为 0 且不重复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 6837 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # 3.其他思路
        # # 时间复杂度: O(n^2)
        # # 空间复杂度: O(n)
        # res = []
        #
        # zero = 0
        # positive = {}
        # negative = {}
        #
        # for num in nums:
        #     if num == 0:
        #         zero += 1
        #     elif num > 0:
        #         positive.setdefault(num, 0)
        #         positive[num] += 1
        #     else:
        #         negative.setdefault(num, 0)
        #         negative[num] += 1
        #
        # if zero >= 3:
        #     res.append([0, 0, 0])
        #
        # for pos in positive:
        #     if positive[pos] >= 2 and (-2*pos) in negative:
        #         res.append([-2*pos, pos, pos])
        #     if zero > 0 and -pos in negative:
        #         res.append([-pos, 0, pos])
        #     for neg in negative:
        #         if -neg <= pos:
        #             continue
        #         pos2 = -neg - pos
        #         if pos2 in positive and pos2 > pos:
        #             res.append([neg, pos, pos2])
        #
        # for neg in negative:
        #     if negative[neg] >= 2 and (-2*neg) in positive:
        #         res.append([neg, neg, -2*neg])
        #     for pos in positive:
        #         if -neg > pos:
        #             continue
        #         neg2 = -pos - neg
        #         if neg2 in negative and neg2 > neg:
        #             res.append([neg, neg2, pos])
        #
        # return res

        # 2.双指针 时间复杂度O(n²) 空间复杂度O(1)
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if (nums[left] + nums[right]) == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
                elif (nums[left] + nums[right]) > target:
                    right -= 1
                else:
                    left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
