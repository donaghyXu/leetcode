# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder 和 postorder 都由 不同 的值组成 
#  postorder 中每一个值都在 inorder 中 
#  inorder 保证是树的中序遍历 
#  postorder 保证是树的后序遍历 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 递归切割
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        return self.build(inorder, postorder)

    def build(self, inorder, postorder):
        if len(postorder) == 0:
            return None

        root_value = postorder[-1]
        root = TreeNode(val=root_value)

        root_index = inorder.index(root_value)
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        root.left = self.build(inorder_left, postorder_left)
        root.right = self.build(inorder_right, postorder_right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
