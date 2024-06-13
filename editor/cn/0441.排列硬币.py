# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。 
# 
#  给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 5
# 输出：2
# 解释：因为第三行不完整，所以返回 2 。
#  
# 
#  示例 2： 
#  
#  
# 输入：n = 8
# 输出：3
# 解释：因为第四行不完整，所以返回 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics 数学 二分查找 👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 二分
        # 时间复杂度：O(logn)
        # 空间复杂度：O(1)
        # 思路：二分查找，根据等差数列求和公式(n²+n)/2求得n行可得的硬币总数来判断

        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if (mid * mid + mid) / 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right
# leetcode submit region end(Prohibit modification and deletion)
