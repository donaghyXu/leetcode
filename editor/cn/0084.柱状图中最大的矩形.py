# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 2711 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        heights.insert(0, 0)
        heights.append(0)
        n = len(heights)
        stack = []
        stack.append(0)
        max_area = 0
        for i in range(n):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        h = heights[mid]
                        w = i - stack[-1] - 1
                        area = h * w
                        max_area = max(area, max_area)
                stack.append(i)
        return max_area
# leetcode submit region end(Prohibit modification and deletion)
