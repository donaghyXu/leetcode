# 
#  
#  给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则
# ，返回 false 。 
#  
#  
# 
#  二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  root 树上的节点数量范围是 [1, 2000] 
#  subRoot 树上的节点数量范围是 [1, 1000] 
#  -10⁴ <= root.val <= 10⁴ 
#  -10⁴ <= subRoot.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 字符串匹配 哈希函数 👍 1023 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 遍历
        # 时间复杂度：O(n²)
        # 空间复杂度：O(1)
        return self.dfs(root, subRoot)

    def dfs(self, node, subRoot):
        if subRoot is None:
            return True
        if node is None and subRoot is not None:
            return False
        if self.compare(node, subRoot):
            return True
        return self.dfs(node.left, subRoot) or self.dfs(node.right, subRoot)

    def compare(self, left, right):
        # 判断中止
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
