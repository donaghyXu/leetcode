# 
#  请你设计并实现一个满足 
#  LRU (最近最少使用) 缓存 约束的数据结构。
#  
# 
#  
#  实现 
#  LRUCache 类：
#  
# 
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
#  
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 10⁵ 
#  最多调用 2 * 10⁵ 次 get 和 put 
#  
# 
#  Related Topics 设计 哈希表 链表 双向链表 👍 3147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # 思路：因为put操作涉及链表删除，而能满足O(1)操作的只有双向链表
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head = DLinkNode()
        self.dummy_tail = DLinkNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0
        self.cache_dict = {}

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.move_to_end(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.value = value
            self.move_to_end(node)
        else:
            if self.size == self.capacity:
                node = self.dummy_head.next
                self.cache_dict.pop(node.key)
                self.move_node(node)
                self.size -= 1
            node = DLinkNode(key, value)
            self.cache_dict[key] = node
            self.add_node(node)
            self.size += 1

    def move_to_end(self, node):
        self.move_node(node)
        self.add_node(node)

    def move_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_node(self, node):
        prev = self.dummy_tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

