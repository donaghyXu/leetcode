# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重
# 叠 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= intervals.length <= 10⁵ 
#  intervals[i].length == 2 
#  -5 * 10⁴ <= starti < endi <= 5 * 10⁴ 
#  
# 
#  Related Topics 贪心 数组 动态规划 排序 👍 1124 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(1)
        # 思路：需要移除区间的最小数量，使剩余区间互不重叠，也就是要保留尽量多的互不重叠的区间
        #      那么就是要使保留的每个区间范围尽可能的小，按照区间的右边界排序，计数，重叠的区间略过

        if len(intervals) == 1:
            return 0
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        cnt = 0
        end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
