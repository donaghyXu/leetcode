# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
# 
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 👍 2499 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划
        # 时间复杂度：O(n²)
        # 空间复杂度：O(n)
        # 思路：由n个节点组成的二叉树分为n种情况，分别是以1为根节点，2为根节点……n为根节点
        #      每种情况的组成数量可以通过左右子树计算得到
        #      以1为根节点，比1小的数没有，所以左子树数量为dp[0]=1
        #      比1大的数有n-1，所以右子树数量为dp[n-1]，所以总数量为dp[0]*dp[n-1]
        #      以2为根节点，比2小的数有1个，所以左子树数量为dp[1]
        #      比2大的数有n-2，所以右子树数量为dp[n-2]，所以总数量为dp[1]*dp[n-2]
        #      以n为根节点，比n小的数有n-1个，所以左子树数量为dp[n-1]
        #      比n大的数没有，所以右子树数量为dp[0]，所以总数量为dp[n-1]*dp[0]
        #      由n个节点组成的二叉搜索树数量即为以上n种情况的叠加

        # dp[i]：由i个节点组成的二叉搜索树有dp[i]种
        dp = [0 for _ in range(n + 1)]

        # 初始化
        dp[0] = 1
        dp[1] = 1

        # 递推，遍历
        # dp[2] = dp[0]*dp[1]+dp[1]*dp[0]
        # dp[3] = dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
        # dp[4] = dp[0]*dp[3]+dp[1]*dp[2]+dp[2]*dp[1]+dp[3]*dp[0]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
