# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
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
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 2072 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 2.迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = []
        stack = []
        cur = root
        while cur is not None or stack:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right
        return res

        # # 1.递归
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # res = []
        #
        # def dfs(node):
        #     if node is None:
        #         return
        #
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        #
        # dfs(root)
        # return res
# leetcode submit region end(Prohibit modification and deletion)
