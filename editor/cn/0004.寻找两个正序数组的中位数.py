# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 7146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 二分查找
        # 时间复杂度：O(log(m+n))
        # 空间复杂度：O(1)
        # 思路：转化成寻找两个有序数组中的第k小的数

        m = len(nums1)
        n = len(nums2)
        left = int((m + n + 1) / 2)
        right = int((m + n + 2) / 2)

        # 相等代表两个数组加起来是奇数，中位数是left
        # 不相等代表两个数组加起来是偶数，中位数是(left+right)/2
        if left == right:
            return self.find_kth(nums1, 0, m - 1, nums2, 0, n - 1, left)
        else:
            return (self.find_kth(nums1, 0, m - 1, nums2, 0, n - 1, left) +
                    self.find_kth(nums1, 0, m - 1, nums2, 0, n - 1, right)) / 2

    def find_kth(self, nums1, start1, end1, nums2, start2, end2, k):
        nums1_len = end1 - start1 + 1
        nums2_len = end2 - start2 + 1

        # 如果一方数组个数为0，那第k小的就是另一方数组的第k小元素
        if nums1_len == 0:
            return nums2[start2 + k - 1]
        if nums2_len == 0:
            return nums1[start1 + k - 1]

        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(nums1_len, k // 2) - 1
        j = start2 + min(nums2_len, k // 2) - 1

        # 如果nums1[k/2]比nums2[k/2]大，那说明nums2的前k/2个元素都比第k个元素小
        if nums1[i] > nums2[j]:
            return self.find_kth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.find_kth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
# leetcode submit region end(Prohibit modification and deletion)
