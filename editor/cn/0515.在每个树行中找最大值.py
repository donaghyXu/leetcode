# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#  
# 
#  示例2： 
# 
#  
# 输入: root = [1,2,3]
# 输出: [1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [0,10⁴] 
#  
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 363 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 层序遍历递归法
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        res = []
        depth = 0
        self.bfs(root, depth, res)
        return [max(x) for x in res]

    def bfs(self, node, depth, res):
        if node is None:
            return
        if len(res) == depth:
            res.append([])
        res[depth].append(node.val)
        self.bfs(node.left, depth + 1, res)
        self.bfs(node.right, depth + 1, res)
# leetcode submit region end(Prohibit modification and deletion)
