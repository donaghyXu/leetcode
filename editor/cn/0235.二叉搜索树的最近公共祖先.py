# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#  
# 
#  示例 2: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。 
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉搜索树中。 
#  
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 1239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2.迭代法
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 思路：利用二叉搜索树的特性，很容易想到二分查找

        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root
        return None

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # 1.深度优先
    #     # 时间复杂度：O(n)
    #     # 空间复杂度：O(n)
    #     if p.val < q.val:
    #         return self.dfs(root, p, q)
    #     else:
    #         return self.dfs(root, q, p)
    #
    # def dfs(self, node, p, q):
    #     if p > node.val:
    #         left = self.dfs(node.left, p, q)
    #         if left is not None:
    #             return left
    #     elif q < node.val:
    #         right = self.dfs(node.right, p, q)
    #         if right is not None:
    #             return right
    #     else:
    #         return node
# leetcode submit region end(Prohibit modification and deletion)
