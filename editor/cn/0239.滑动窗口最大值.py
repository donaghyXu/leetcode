# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。 
# 
#  返回 滑动窗口中的最大值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], k = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 👍 2770 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, x):
        if x == self.queue[0]:
            self.queue.popleft()

    def push(self, x):
        while self.queue and x > self.queue[-1]:
            self.queue.pop()
        self.queue.append(x)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2.单调队列
        # 时间复杂度：O(n)
        # 空间复杂度：O(k)
        n = len(nums)
        if n <= k:
            return [max(nums)]

        result = []
        queue = MyQueue()
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())

        for i in range(k, n):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            result.append(queue.front())
        return result

        # # 1.双指针 会超时
        # # 时间复杂度：O(n*k)
        # # 空间复杂度：O(n-k)
        # if len(nums) < k:
        #     return [max(nums)]
        # left = 0
        # right = left + k - 1
        # res = []
        # while right < len(nums):
        #     max_num = max(nums[left:(right+1)])
        #     res.append(max_num)
        #     left += 1
        #     right += 1
        # return res
# leetcode submit region end(Prohibit modification and deletion)
