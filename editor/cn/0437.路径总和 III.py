# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 
# 
#  路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,1000] 
#  
#  -10⁹ <= Node.val <= 10⁹ 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1863 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 2.前缀和+dfs
    # 时间复杂度：O(n）
    # 空间复杂度：O(n)
    def __init__(self):
        self.result = 0
        self.count = defaultdict(int)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count[0] = 1
        self.dfs(root, 0, targetSum)
        return self.result

    def dfs(self, node, s, targetSum):
        if node is None:
            return

        s += node.val
        self.result += self.count[s - targetSum]
        self.count[s] += 1
        self.dfs(node.left, s, targetSum)
        self.dfs(node.right, s, targetSum)
        self.count[s] -= 1

    # # 1.dfs
    # # 时间复杂度：O(n²）
    # # 空间复杂度：O(n)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     if root is None:
    #         return 0
    #     count = self.dfs(root, targetSum)
    #     count += self.pathSum(root.left, targetSum)
    #     count += self.pathSum(root.right, targetSum)
    #     return count

    # def dfs(self, node, targetSum):
    #     if node is None:
    #         return 0

    #     count = 0
    #     if node.val == targetSum:
    #         count += 1

    #     count += self.dfs(node.left, targetSum - node.val)
    #     count += self.dfs(node.right, targetSum - node.val)
    #     return count
# leetcode submit region end(Prohibit modification and deletion)
