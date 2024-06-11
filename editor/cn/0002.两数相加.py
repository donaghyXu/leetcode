# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。 
# 
#  请你将两个数相加，并以相同形式返回一个表示和的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个链表中的节点数在范围 [1, 100] 内 
#  0 <= Node.val <= 9 
#  题目数据保证列表表示的数字不含前导零 
#  
# 
#  Related Topics 递归 链表 数学 👍 10543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针
        # 时间复杂度：O(max(len(l1), len(l2)))
        # 空间复杂度：O(max(len(l1), len(l2)))
        # 思路：单链表模拟算术加法，
        #      carry 模拟进位 0或1
        #      carry大于0的条件是因为结果可能比数字位数多出一位
        #      所以数字位数遍历完后可能还没结束，如99,1-> 99+01=100
        #      转换成数相加不适用于超长整数情况
        carry = 0
        dummy_head = ListNode(0)
        cur = dummy_head

        while l1 or l2 or carry:
            sum_value = carry
            sum_value += l1.val if l1 else 0
            sum_value += l2.val if l2 else 0

            carry = 1 if sum_value > 9 else 0

            if carry == 1:
                remain = sum_value - 10
            else:
                remain = sum_value
            cur.next = ListNode(remain)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
# leetcode submit region end(Prohibit modification and deletion)
