# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
# 
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 2826 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 优先队列
        # 时间复杂度：O(m*logn)，m为总元素个数；n为lists长度，也就是优先队列的最大长度
        #                      其插入删除的时间复杂度为O(logn)
        # 空间复杂度：O(n)
        min_heapq = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heapq, (node.val, i, node))

        dummy_head = ListNode()
        cur = dummy_head
        while min_heapq:
            val, index, node = heapq.heappop(min_heapq)

            cur.next = ListNode(val)
            cur = cur.next

            if node.next:
                heapq.heappush(min_heapq, (node.next.val, index, node.next))

        return dummy_head.next
# leetcode submit region end(Prohibit modification and deletion)
