# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。 
# 
#  找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  返回容器可以储存的最大水量。 
# 
#  说明：你不能倾斜容器。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  示例 2： 
# 
#  
# 输入：height = [1,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  2 <= n <= 10⁵ 
#  0 <= height[i] <= 10⁴ 
#  
# 
#  Related Topics 贪心 数组 双指针 👍 5000 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针，贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：先使求面积的宽度最大，即left=0,right=n-1
        #      高度小的那侧肯定不如高度大的那侧求面积贡献大
        #      因此将高度小的那侧往里收缩一个单位，不断循环直到left和right相遇
        n = len(height)
        max_water = 0
        left = 0
        right = n - 1
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            # 高度小的往里面收缩
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
# leetcode submit region end(Prohibit modification and deletion)
