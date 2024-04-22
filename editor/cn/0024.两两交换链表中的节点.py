# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics 递归 链表 👍 2195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 模拟
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head

        while cur.next is not None and cur.next.next is not None:
            temp = cur.next.next
            cur.next.next = temp.next
            temp.next = cur.next
            cur.next = temp

            cur = cur.next.next
        return dummy_head.next
# leetcode submit region end(Prohibit modification and deletion)
