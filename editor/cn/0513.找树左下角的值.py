# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 
# 
#  假设二叉树中至少有一个节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1,10⁴] 
#  
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 574 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 2.层序遍历 迭代法
        # 时间复杂度：O(n)
        # 空间复杂度：O(h)
        queue = deque()
        queue.append(root)
        res = 0

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return res

    # def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    #     # 1.层序遍历 递归法
    #     # 时间复杂度：O(n)
    #     # 空间复杂度：O(h)
    #     res = []
    #     depth = 0
    #     self.bfs(root, depth, res)
    #     return res[-1][0]
    #
    # def bfs(self, node, depth, res):
    #     if node is None:
    #         return
    #     if len(res) == depth:
    #         res.append([])
    #     res[depth].append(node.val)
    #     self.bfs(node.left, depth+1, res)
    #     self.bfs(node.right, depth+1, res)

# leetcode submit region end(Prohibit modification and deletion)
