# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为
#  root 。 
# 
#  除了
#  root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的
# 房子在同一天晚上被打劫 ，房屋将自动报警。 
# 
#  给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [3,2,3,null,3,null,1]
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: root = [3,4,5,1,3,null,1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  树的节点数在 [1, 10⁴] 范围内 
#  0 <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 1973 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 动态规划 深搜 后序遍历
        # 时间复杂度：O(n)
        # 空间复杂度：O(1ogn)
        result = self.dfs(root)
        return max(result)

    def dfs(self, node):
        # 长度为2的数组，0为不偷，1为不偷
        if node is None:
            return [0, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 不偷
        val1 = max(left[0], left[1]) + max(right[0], right[1])

        # 偷
        val2 = node.val + left[0] + right[0]
        return [val1, val2]

    # def rob(self, root: Optional[TreeNode]) -> int:
    #     # 动态规划 深搜 后序遍历
    #     # 时间复杂度：O(n)
    #     # 空间复杂度：O(1ogn)
    #     _, result, _ = self.dfs(root)
    #     return result
    #
    # def dfs(self, node):
    #     if node is None:
    #         return 0, 0, True
    #     if node.left is None and node.right is None:
    #         return 0, node.val, True
    #
    #     left_pre, left, left_flag = self.dfs(node.left)
    #     right_pre, right, right_flag = self.dfs(node.right)
    #
    #     pre = left + right
    #     if left_flag and right_flag:  # 没有孙子了，只和孩子比较
    #         return pre, max(left + right, node.val), False
    #     else:
    #         pre_pre = left_pre + right_pre  # 有孙子，比较孙子+自己和孩子两个状态
    #         return pre, max(pre, pre_pre + node.val), False

# leetcode submit region end(Prohibit modification and deletion)
