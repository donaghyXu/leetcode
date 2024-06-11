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
        # 2.双指针
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)
        # 思路：通过双指针将三层for循环降为两层，固定一个数，另外两个数通过双指针查找
        nums.sort()
        n = len(nums)
        result = []

        # min_max剪枝，最小值比目标值还大，最大值比目标值还小，都不可能找到符合目标值的结果
        min_value = nums[0] + nums[1] + nums[2]
        max_value = nums[-1] + nums[-2] + nums[-3]
        if min_value > 0 or max_value < 0:
            return result

        for i in range(n - 2):
            # 剪枝，第一个数相同的情况
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 剪枝，第一个数大于0，整体之和大于0，找不到等于0的情况
            if nums[i] > 0:
                break

            target = -nums[i]
            left = i + 1
            right = n - 1

            # min_max剪枝，最小值比目标值还大，最大值比目标值还小，都不可能找到符合目标值的结果
            min_value = nums[i] + nums[left] + nums[left + 1]
            max_value = nums[i] + nums[right] + nums[right - 1]
            if min_value > 0 or max_value < 0:
                continue

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # 剪枝，去除第二个数重复的情况
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    # 剪枝，去除第三个数重复的情况
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result

        # # 1.哈希表，组合分析
        # # 时间复杂度: O(n²)
        # # 空间复杂度: O(n)
        # # 思路：总和为0，可以分成四种情况
        # #      第一种为0，0，0
        # #      第二种为正，0，负
        # #      第三种为正，正，负
        # #      第四种为正，负，负
        # #      对每种情况分别判断可得结果
        #
        # res = []
        #
        # zero = 0
        # positive = collections.defaultdict(int)
        # negative = collections.defaultdict(int)
        #
        # for num in nums:
        #     if num == 0:
        #         zero += 1
        #     elif num > 0:
        #         positive[num] += 1
        #     else:
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
# leetcode submit region end(Prohibit modification and deletion)
