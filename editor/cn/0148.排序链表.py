# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
# 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 2315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 排序
        # 时间复杂度：O(nlogn)
        # 空间复杂度：O(n)
        # 思路：将node与自身的值绑定，将值作为key排序，并重新建立关联

        if head is None:
            return None
        link_list = []
        cur = head

        # 将节点与值绑定
        while cur:
            link_list.append((cur.val, cur))
            cur = cur.next

        # 排序
        link_list.sort(key=lambda x: x[0])
        n = len(link_list)

        # 重新建立关联
        for i in range(n - 1):
            link_list[i][1].next = link_list[i + 1][1]
        link_list[n - 1][1].next = None
        return link_list[0][1]
# leetcode submit region end(Prohibit modification and deletion)
