# 给定一个二叉树 root ，返回其最大深度。 
# 
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,null,2]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在 [0, 10⁴] 区间内。 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1815 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 遍历 dfs
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        self.dfs(root, 1)
        return self.max_depth

    def dfs(self, node, depth):
        if node is None:
            return

        self.max_depth = max(self.max_depth, depth)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
# leetcode submit region end(Prohibit modification and deletion)
