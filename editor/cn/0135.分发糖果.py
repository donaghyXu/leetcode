# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。 
# 
#  你需要按照以下要求，给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  相邻两个孩子评分更高的孩子会获得更多的糖果。 
#  
# 
#  请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2： 
# 
#  
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。 
# 
#  
# 
#  提示： 
# 
#  
#  n == ratings.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= ratings[i] <= 2 * 10⁴ 
#  
# 
#  Related Topics 贪心 数组 👍 1486 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：两轮遍历，第一轮从左到右，如果右边的孩子比左高，那就数量+1
        #      为了不影响第一遍排好的顺序，第二轮从右往左遍历
        #      如果左边的孩子比右边高，那就在右边的数量上+1
        #      因为右侧的必然比左侧的高，所以+1后依旧比左侧高，此时又比右侧高
        #      满足题目条件

        n = len(ratings)
        result = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
                result[i] = result[i + 1] + 1
        return sum(result)
# leetcode submit region end(Prohibit modification and deletion)
