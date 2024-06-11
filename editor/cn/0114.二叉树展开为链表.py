# 给你二叉树的根结点 root ，请你将它展开为一个单链表： 
# 
#  
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
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
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 链表 二叉树 👍 1682 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 前序遍历，哈希表
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        if root is None:
            return None
        hash_dict = []
        self.dfs(root, hash_dict)
        n = len(hash_dict)
        for i in range(n - 1):
            hash_dict[i].right = hash_dict[i + 1]
            hash_dict[i].left = None
        hash_dict[n - 1].right = None

    def dfs(self, node, hash_dict):
        if node is None:
            return

        hash_dict.append(node)
        self.dfs(node.left, hash_dict)
        self.dfs(node.right, hash_dict)
# leetcode submit region end(Prohibit modification and deletion)
