# 给定一个二叉树，判断它是否是 平衡二叉树 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1499 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 后序遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if root is None:
            return True
        return self.get_height(root)[0]

    def get_height(self, node):
        if node is None:
            return True, 0
        left_flag, left = self.get_height(node.left)
        right_flag, right = self.get_height(node.right)
        if abs(left - right) <= 1:
            return True and left_flag and right_flag, max(left, right) + 1
        else:
            return False, max(left, right) + 1
# leetcode submit region end(Prohibit modification and deletion)
