# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
# 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 👍 1823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 2.大根堆
        # 时间复杂度：O(nlogk)
        # 空间复杂度：O(n)

        # 统计元素出现频率
        hash_dict = collections.defaultdict(int)
        for num in nums:
            hash_dict[num] += 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in hash_dict.items():
            heapq.heappush(pri_que, (freq, key))
            # 如果堆的大小大于了K，则队列弹出当前最小的元素，保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

        # # 1.排序
        # # 时间复杂度：O(nlogn)
        # # 空间复杂度：O(n)
        # # 思路：统计出现频率，按照出现频率排序
        #
        # key_dict = {}
        # for num in nums:
        #     if num in key_dict:
        #         key_dict[num] += 1
        #     else:
        #         key_dict[num] = 1
        #
        # key_dict_items = sorted(key_dict.items(), key=lambda x: -x[1])
        #
        # res = []
        # for key, value in key_dict_items:
        #     res.append(key)
        #     if len(res) == k:
        #         break
        # return res
# leetcode submit region end(Prohibit modification and deletion)
