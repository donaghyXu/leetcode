# 你可以选择使用单链表或者双链表，设计并实现自己的链表。 
# 
#  单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。 
# 
#  如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。 
# 
#  实现 MyLinkedList 类： 
# 
#  
#  MyLinkedList() 初始化 MyLinkedList 对象。 
#  int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。 
#  void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。 
#  void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。 
#  void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 
# index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。 
#  void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", 
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# 输出
# [null, null, null, null, 2, null, 3]
# 
# 解释
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
# myLinkedList.get(1);              // 返回 2
# myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
# myLinkedList.get(1);              // 返回 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= index, val <= 1000 
#  请不要使用内置的 LinkedList 库。 
#  调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。 
#  
# 
#  Related Topics 设计 链表 👍 1014 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_node = Node(0)
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count or index < 0:
            return -1
        cur = self.dummy_node.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        add_node = Node(val)
        add_node.next = self.dummy_node.next
        self.dummy_node.next = add_node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        add_node = Node(val)
        cur = self.dummy_node
        for i in range(self.count):
            cur = cur.next
        cur.next = add_node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.count:
            if index == self.count:
                self.addAtTail(val)
            else:
                add_node = Node(val)
                cur = self.dummy_node
                for i in range(index):
                    cur = cur.next
                add_node.next = cur.next
                cur.next = add_node
                self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.count:
            cur = self.dummy_node
            for i in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
