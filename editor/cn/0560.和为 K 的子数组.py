# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。 
# 
#  子数组是数组中元素的连续非空序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 2378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和，哈希
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        hash_dict = {}
        hash_dict[0] = 1

        count = 0
        num_sum = 0
        for num in nums:
            num_sum += num
            if num_sum - k in hash_dict:
                count += hash_dict[num_sum - k]

            if num_sum in hash_dict:
                hash_dict[num_sum] += 1
            else:
                hash_dict[num_sum] = 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
