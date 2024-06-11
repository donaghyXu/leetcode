# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 2449 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 计数排序
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 思路：统计数的范围
        #      根据计数排序，还需统计数的范围
        #      设定max-min+1的0值数组长度，且统计数时下标刚好-min来衡量
        #      本题已明确表明nums[i]范围为-10000-10000 因此可设定数组长度为20001

        count = [0] * 20001
        # 统计数组中每个值出现的次数
        for num in nums:
            count[num + 10000] += 1

        # 因为要找数组中第k个最大的元素，因此从后往前遍历 寻找第k个最大的
        cnt = 0
        for i in range(len(count) - 1, -1, -1):
            cnt += count[i]
            if cnt >= k:
                return i - 10000
# leetcode submit region end(Prohibit modification and deletion)
