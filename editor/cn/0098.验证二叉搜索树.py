# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 
# 
#  有效 二叉搜索树定义如下： 
# 
#  
#  节点的左子树只包含 小于 当前节点的数。 
#  节点的右子树只包含 大于 当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [2,1,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在[1, 10⁴] 内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 2322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_value = -float('inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归 中序遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 思路：二叉搜索树的中序遍历是递增序列
        return self.dfs(root)

    def dfs(self, node):
        if node is None:
            return True

        left = self.dfs(node.left)
        if node.val > self.max_value:
            self.max_value = node.val
        else:
            return False
        right = self.dfs(node.right)
        return left and right
# leetcode submit region end(Prohibit modification and deletion)
