# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。 
# 
#  
#  例如 arr = [2,3,4] 的中位数是 3 。 
#  例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。 
#  
# 
#  实现 MedianFinder 类: 
# 
#  
#  MedianFinder() 初始化 MedianFinder 对象。 
#  void addNum(int num) 将数据流中的整数 num 添加到数据结构中。 
#  double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10⁻⁵ 以内的答案将被接受。 
#  
# 
#  示例 1： 
# 
#  
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
# 
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0 
# 
#  提示: 
# 
#  
#  -10⁵ <= num <= 10⁵ 
#  在调用 findMedian 之前，数据结构中至少有一个元素 
#  最多 5 * 10⁴ 次调用 addNum 和 findMedian 
#  
# 
#  Related Topics 设计 双指针 数据流 排序 堆（优先队列） 👍 982 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
class MedianFinder:
    # 大根堆，小根堆
    # 思路：通过维护两个平衡的大根堆，小根堆，来获取中间值
    #      如果总数是奇数，即小根堆数量大于大根堆，那么取小根堆的堆顶
    #      如果总数是偶数，即小根堆数量等于大根堆，那么取小根堆和大根堆的堆顶
    def __init__(self):
        self.heap_min = []
        self.heap_max = []

    def addNum(self, num: int) -> None:
        if not self.heap_min or num <= -self.heap_min[0]:
            heapq.heappush(self.heap_min, -num)
            if len(self.heap_max) + 1 < len(self.heap_min):
                heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
        else:
            heapq.heappush(self.heap_max, num)
            if len(self.heap_max) > len(self.heap_min):
                heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))

    def findMedian(self) -> float:
        if len(self.heap_min) > len(self.heap_max):
            return -self.heap_min[0]
        else:
            return (-self.heap_min[0] + self.heap_max[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
