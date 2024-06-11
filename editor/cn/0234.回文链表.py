# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  Related Topics 栈 递归 链表 双指针 👍 1912 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 链表 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 思路：找到中间值，截断，反转后面一段
        #      逐个遍历判断

        # 找到中间值
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next
        mid = int(list_len / 2)

        # 反转后一段链表
        count = 0
        cur = head
        while cur and count < mid:
            count += 1
            cur = cur.next
        right_start = self.reverse_list(cur)

        # 逐个遍历判断是否相等
        count = 0
        left_cur = head
        right_cur = right_start
        while left_cur and count < mid:
            count += 1
            if left_cur.val != right_cur.val:
                return False
            left_cur = left_cur.next
            right_cur = right_cur.next
        return True

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
