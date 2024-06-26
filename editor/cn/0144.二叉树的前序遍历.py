# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
#  
#  
# 输入：root = [1,2]
# 输出：[1,2]
#  
# 
#  示例 5： 
#  
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 2. 迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res

        # # 1. 递归
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # res = []
        #
        # def dfs(node):
        #     if node is None:
        #         return
        #
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        #
        # dfs(root)
        # return res
# leetcode submit region end(Prohibit modification and deletion)
