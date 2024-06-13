# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,null,3]
# 输出: [1,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1059 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 2.广度优先，bfs，递归法
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        level = 0
        result = []
        self.bfs(root, level, result)
        return [x[-1] for x in result]

    def bfs(self, node, level, result):
        if node is None:
            return

        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        self.bfs(node.left, level + 1, result)
        self.bfs(node.right, level + 1, result)

    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     # 1.广度优先，bfs，迭代法
    #     # 时间复杂度：O(n)
    #     # 空间复杂度：O(n)
    #
    #     if root is None:
    #         return []
    #
    #     queue = collections.deque()
    #     queue.append([root])
    #     result = []
    #
    #     while queue:
    #         node_list = queue.popleft()
    #         len_node_list = len(node_list)
    #         level = []
    #         for i in range(len_node_list):
    #             node = node_list[i]
    #             if node.left:
    #                 level.append(node.left)
    #             if node.right:
    #                 level.append(node.right)
    #         if len(level) > 0:
    #             queue.append(level)
    #         result.append(node_list[-1].val)
    #     return result
# leetcode submit region end(Prohibit modification and deletion)
