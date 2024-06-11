# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现
# 次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
# 
#  Related Topics 数组 哈希表 双指针 二分查找 排序 👍 1037 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 2.哈希表
        # 时间复杂度：O(max(len(nums1), len(nums2)))
        # 空间复杂度：O(max(len(nums1), len(nums2)))
        nums1_dict = collections.defaultdict(int)
        nums2_dict = collections.defaultdict(int)
        for num in nums1:
            nums1_dict[num] += 1
        for num in nums2:
            nums2_dict[num] += 1

        result = []
        for key, value in nums1_dict.items():
            if key in nums2_dict:
                same_num = min(value, nums2_dict[key])
                for i in range(same_num):
                    result.append(key)
        return result

        # 1.内置函数
        # # 时间复杂度：O(max(len(nums1), len(nums2)))
        # # 空间复杂度：O(max(len(nums1), len(nums2)))
        # nums1_count = Counter(nums1)
        # nums2_count = Counter(nums2)
        # res_set = set(nums1).intersection(set(nums2))
        # res = []
        # for element in res_set:
        #     cnt = min(nums1_count[element], nums2_count[element])
        #     res.extend([element] * cnt)
        # return res
# leetcode submit region end(Prohibit modification and deletion)
