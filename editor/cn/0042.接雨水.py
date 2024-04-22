# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 5135 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针 按照列的方向来计算
        # 时间复杂度：O(n)
        # 空间复杂度：
        n = len(height)
        left_max_height = [0] * n
        right_max_height = [0] * n

        left_max_height[0] = height[0]
        for i in range(1, n):
            left_max_height[i] = max(left_max_height[i - 1], height[i])
        right_max_height[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max_height[i] = max(right_max_height[i + 1], height[i])

        total_rain = 0
        for i in range(1, n - 1):
            rain = min(left_max_height[i], right_max_height[i]) - height[i]
            total_rain += rain
        return total_rain

        # # 单调栈 按照行的方向计算雨水
        # # 从栈顶到栈底的顺序：从小到大
        # # 通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
        # # 雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
        # # 雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # n = len(height)
        # if n <= 2:
        #     return 0
        # stack = []
        #
        # rain_total = 0
        # stack.append(0)
        # for i in range(1, n):
        #     if height[i] < height[stack[-1]]:
        #         stack.append(i)
        #     elif height[i] == height[stack[-1]]:
        #         stack.pop()
        #         stack.append(i)
        #     else:
        #         while stack and height[i] > height[stack[-1]]:
        #             mid = stack.pop()
        #             if stack:
        #                 h = min(height[stack[-1]], height[i]) - height[mid]
        #                 w = i - stack[-1] - 1
        #                 rain_total += (h * w)
        #         stack.append(i)
        # return rain_total
# leetcode submit region end(Prohibit modification and deletion)
