# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 100 
#  
# 
#  Related Topics 数组 二分查找 动态规划 滑动窗口 哈希函数 滚动哈希 👍 1071 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(nums1_len*nums2_len)
        # 空间复杂度：O(nums1_len*nums2_len)

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        # dp[i][j]：到下标i-1的数组1和到下标j-1的数组2的最长公共子数组长度
        dp = [[0 for _ in range(nums2_len + 1)] for _ in range(nums1_len + 1)]

        result = 0
        # 递推，遍历
        for i in range(1, nums1_len + 1):
            for j in range(1, nums2_len + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result, dp[i][j])
        return result
# leetcode submit region end(Prohibit modification and deletion)
