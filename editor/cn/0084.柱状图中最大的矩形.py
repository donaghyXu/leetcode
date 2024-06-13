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
        # 思路：栈底到栈顶为递增，遇到下一个比栈顶元素小的时候，计算面积
        #      先计算栈顶列的面积，再往左拓展，拓展的面积的高度由拓展的那列高度决定
        #      拓展的面积的宽度是栈顶列到拓展列的长度

        # 防止序列是递增的，无法触发面积计算
        heights.insert(0, 0)
        # 防止序列是递减的，错过第一列面积计算
        heights.append(0)

        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            if stack:
                if heights[i] > heights[stack[-1]]:
                    stack.append(i)
                elif heights[i] == heights[stack[-1]]:
                    stack.pop()
                    stack.append(i)
                else:
                    while stack and heights[i] < heights[stack[-1]]:
                        mid = stack.pop()
                        if stack:
                            w = i - stack[-1] - 1
                            h = heights[mid]
                            area = w * h
                            max_area = max(max_area, area)
                    stack.append(i)
            else:
                stack.append(i)
        return max_area
# leetcode submit region end(Prohibit modification and deletion)
