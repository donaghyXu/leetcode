# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁴ 
#  
# 
#  Related Topics 数组 排序 👍 2273 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 贪心
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        # 思路：先按左边界排序，让所有的相邻区间尽可能的重叠在一起
        #      按照左边界从小到大排序之后，如果 intervals[i][0] <= intervals[i - 1][1]
        #      即intervals[i]的左边界 <= intervals[i - 1]的右边界，则一定有重叠
        #      合并区间，即将intervals[i]的右边界作为新的右边界，不断更新

        intervals.sort(key=lambda x: x[0])
        result = []
        # 起始区间的左、右边界
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # 更新右边界
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                # 到新的区间，将之前的区间添加到result中
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result
# leetcode submit region end(Prohibit modification and deletion)