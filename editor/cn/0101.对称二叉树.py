# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2695 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # 首先排除空节点的情况
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        # 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val:
            return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside
# leetcode submit region end(Prohibit modification and deletion)
