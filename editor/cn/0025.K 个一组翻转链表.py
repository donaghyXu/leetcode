# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  
# 提示：
# 
#  
#  链表中的节点数目为 n 
#  1 <= k <= n <= 5000 
#  0 <= Node.val <= 1000 
#  
# 
#  
# 
#  进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？ 
# 
#  
#  
# 
#  Related Topics 递归 链表 👍 2337 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 模拟
        # 时间复杂度：O(nk)
        # 空间复杂度：O(1)
        # 思路：每k个节点，缓存第一个节点的前一个节点和最后一个节点的后一个节点
        #      断掉这k个节点与前面和后面的相连之处
        #      反转链表，再恢复与前面一段的相连，与后面一段的相连
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head.next
        prev = dummy_head
        count = 1
        while cur:
            if count % k == 0:
                # 缓存k个节点的之后一个节点
                next_node = cur.next
                # 断掉连接
                cur.next = None
                # 反转链表
                new_head = self.reverse_list(prev.next)
                # 恢复链接
                new_tail = prev.next
                new_tail.next = next_node
                prev.next = new_head
                # 缓存下一个k个节点的之前一个节点
                prev = new_tail
                cur = prev
            cur = cur.next
            count += 1
        return dummy_head.next

    def reverse_list(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
# leetcode submit region end(Prohibit modification and deletion)
