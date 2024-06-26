# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组： 
# 
#  
#  选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。 
#  
# 
#  重复这个过程恰好 k 次。可以多次选择同一个下标 i 。 
# 
#  以这种方式修改数组后，返回数组 可能的最大和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -100 <= nums[i] <= 100 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics 贪心 数组 排序 👍 440 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        # 思路：先按绝对值大小降序排序，要想使和最大，就需要尽量操作最小的那个数
        #      对于负数来说，绝对值越大，值越小，反转后对于总和贡献最大
        #      先使所有的负数变为正数，如果k还没消耗完，就重复操作最小的那个数
        nums.sort(key=lambda x: -abs(x))
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = - nums[i]
                k -= 1
            if k == 0:
                return sum(nums)
        if k % 2 == 1:
            nums[-1] = -nums[-1]
        return sum(nums)
# leetcode submit region end(Prohibit modification and deletion)

