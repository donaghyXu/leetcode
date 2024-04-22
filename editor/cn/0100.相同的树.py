# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#  
# 
#  示例 3： 
#  
#  
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树上的节点数目都在范围 [0, 100] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        return self.compare(p, q)

    def compare(self, left, right):
        # 判断中止条件
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        # 递归
        l = self.compare(left.left, right.left)
        r = self.compare(left.right, right.right)
        return l and r
# leetcode submit region end(Prohibit modification and deletion)
