# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
# 
#  Related Topics 链表 双指针 👍 2847 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2.双指针法
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        pre = ListNode(0, head)
        slow = pre
        fast = pre
        cnt = 0
        while fast is not None:
            cnt += 1
            fast = fast.next
            if cnt > (n + 1):
                slow = slow.next
        slow.next = slow.next.next
        return pre.next

        # # 1.模拟法
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # cnt = 0
        # new_head = head
        # while new_head is not None:
        #     cnt += 1
        #     new_head = new_head.next
        #
        # pre = ListNode(0, head)
        # new_head = pre
        # index = 0
        # while new_head is not None:
        #     index += 1
        #     if index == (cnt - n + 1):
        #         new_head.next = new_head.next.next
        #         break
        #     new_head = new_head.next
        # return pre.next
# leetcode submit region end(Prohibit modification and deletion)
