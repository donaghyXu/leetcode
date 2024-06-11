# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：["1"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 1121 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 深度优先
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = []
        res_final = []
        if root is None:
            return []
        self.dfs(root, res, res_final)
        return res_final

    def dfs(self, node, res, res_final):
        res.append(node.val)

        # 终止条件
        if node.left is None and node.right is None:
            s = '->'.join(map(str, res))
            res_final.append(s)
            return

        # 单层处理逻辑
        if node.left:
            self.dfs(node.left, res, res_final)
            res.pop()
        if node.right:
            self.dfs(node.right, res, res_final)
            res.pop()
# leetcode submit region end(Prohibit modification and deletion)
