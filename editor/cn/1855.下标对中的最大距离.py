# 给你两个 非递增 的整数数组 nums1 和 nums2 ，数组下标均 从 0 开始 计数。 
# 
#  下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= 
# j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i 。 
# 
#  返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。 
# 
#  一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
# 输出：2
# 解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
# 最大距离是 2 ，对应下标对 (2,4) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [2,2,2], nums2 = [10,10,1]
# 输出：1
# 解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
# 最大距离是 1 ，对应下标对 (0,1) 。 
# 
#  示例 3： 
# 
#  
# 输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
# 输出：2
# 解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
# 最大距离是 2 ，对应下标对 (2,4) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= 10⁵ 
#  1 <= nums2.length <= 10⁵ 
#  1 <= nums1[i], nums2[j] <= 10⁵ 
#  nums1 和 nums2 都是 非递增 数组 
#  
# 
#  Related Topics 数组 双指针 二分查找 👍 75 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # 二分查找
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        # 思路：每次在nums2数组中用二分查找大于nums1当前值的最大值，计算其距离，不断更新

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        result = 0
        for i in range(nums1_len):
            target = nums1[i]
            left = 0
            right = nums2_len - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right >= i:
                result = max(result, right - i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
