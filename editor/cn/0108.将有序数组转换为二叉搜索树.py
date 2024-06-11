# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
#  
# 
#  示例 2： 
#  
#  
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 按 严格递增 顺序排列 
#  
# 
#  Related Topics 树 二叉搜索树 数组 分治 二叉树 👍 1501 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 二分建树
        # 时间复杂度：O(n)
        # 空间复杂度：O(logn)
        return self.build(nums)

    def build(self, nums):
        if len(nums) == 0:
            return None

        mid = int(len(nums) / 2)
        root = TreeNode(val=nums[mid])
        if len(nums) == 1:
            return root

        root.left = self.build(nums[:mid])
        root.right = self.build(nums[mid+1:])
        return root
# leetcode submit region end(Prohibit modification and deletion)
