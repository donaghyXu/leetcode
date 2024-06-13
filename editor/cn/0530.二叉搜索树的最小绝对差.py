# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  差值是一个正数，其数值等于两值之差的绝对值。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [2, 10⁴] 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-
# nodes/ 相同 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 👍 554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 思路：二叉搜索树中序遍历为有序序列，最小值只可能存在于相邻两个元素的差值之间

        res = []
        self.dfs(root, res)
        min_value = float('inf')
        for i in range(len(res) - 1):
            min_value = min(res[i + 1] - res[i], min_value)
        return min_value

    def dfs(self, node, res):
        if node is None:
            return

        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
# leetcode submit region end(Prohibit modification and deletion)
