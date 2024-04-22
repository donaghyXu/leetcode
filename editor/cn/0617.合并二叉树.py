# 给你两棵二叉树： root1 和 root2 。 
# 
#  想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠
# ，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。 
# 
#  返回合并后的二叉树。 
# 
#  注意: 合并过程必须从两个树的根节点开始。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# 输出：[3,4,5,5,4,null,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：root1 = [1], root2 = [1,2]
# 输出：[2,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树中的节点数目在范围 [0, 2000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1393 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 深度遍历 递归法 新建节点
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode()
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

        # # 深度遍历 递归法 复用原有节点
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        #
        # return root1

        # # 层序遍历 迭代法
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # if root1 is None:
        #     return root2
        # if root2 is None:
        #     return root1
        #
        # queue = deque()
        # queue.append(root1)
        # queue.append(root2)
        #
        # while queue:
        #     node1 = queue.popleft()
        #     node2 = queue.popleft()
        #     node1.val += node2.val
        #
        #     if node1.left is not None and node2.left is not None:
        #         queue.append(node1.left)
        #         queue.append(node2.left)
        #
        #     if node1.right is not None and node2.right is not None:
        #         queue.append(node1.right)
        #         queue.append(node2.right)
        #
        #     if node1.left is None and node2.left is not None:
        #         node1.left = node2.left
        #     if node1.right is None and node2.right is not None:
        #         node1.right = node2.right
        #
        # return root1
# leetcode submit region end(Prohibit modification and deletion)
