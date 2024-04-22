# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。 
# 
#  一般来说，删除节点可分为两个步骤： 
# 
#  
#  首先找到需要删除的节点； 
#  如果找到了，删除它。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,3,6,2,4,null,7], key = 3
# 输出：[5,4,6,2,null,null,7]
# 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
# 另一个正确答案是 [5,2,6,null,4,null,7]。
# 
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,7], key = 0
# 输出: [5,3,6,2,4,null,7]
# 解释: 二叉树不包含值为 0 的节点
#  
# 
#  示例 3: 
# 
#  
# 输入: root = [], key = 0
# 输出: [] 
# 
#  
# 
#  提示: 
# 
#  
#  节点数的范围 [0, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  节点值唯一 
#  root 是合法的二叉搜索树 
#  -10⁵ <= key <= 10⁵ 
#  
# 
#  
# 
#  进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。 
# 
#  Related Topics 树 二叉搜索树 二叉树 👍 1329 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 深度优先
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        return self.dfs(root, key)

    def dfs(self, node, key):
        if node is None:
            return node

        if node.val == key:
            # 叶子节点
            if node.left is None and node.right is None:
                return None

            # 左空右非空
            elif node.left is None and node.right is not None:
                return node.right

            # 左非空右空
            elif node.left is not None and node.right is None:
                return node.left

            # 左右都非空
            else:
                cur = node.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = node.left
                return node.right

        if node.val < key:
            node.right = self.dfs(node.right, key)
        if node.val > key:
            node.left = self.dfs(node.left, key)
        return node
# leetcode submit region end(Prohibit modification and deletion)
