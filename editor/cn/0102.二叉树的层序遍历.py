# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：[[1]]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 2000] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 广度优先搜索 二叉树 👍 1941 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 2. 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(h)
        result = []
        self.dfs(root, result, 0)
        return result

    def dfs(self, node, result, depth):
        if node is None:
            return

        if len(result) == depth:
            result.append([])
        result[depth].append(node.val)
        self.dfs(node.left, result, depth + 1)
        self.dfs(node.right, result, depth + 1)

        # # 1. 迭代法
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(h)
        # result = []
        # queue = collections.deque()
        #
        # if root is None:
        #     return result
        # queue.append(root)
        #
        # while queue:
        #     level = []
        #     level_len = len(queue)
        #     for i in range(level_len):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left is not None:
        #             queue.append(node.left)
        #         if node.right is not None:
        #             queue.append(node.right)
        #     result.append(level)
        # return result
# leetcode submit region end(Prohibit modification and deletion)
