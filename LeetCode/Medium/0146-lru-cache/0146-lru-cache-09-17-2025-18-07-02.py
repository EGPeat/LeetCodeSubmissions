class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-2, -2, self.head, None)
        self.head.next = self.tail
        self.lru = {}
        self.size = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lru.keys():
            return -1
        curr = self.lru[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr.next = self.head.next
        curr.prev = self.head
        self.head.next = curr
        curr.next.prev = curr
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru.keys():
            curr = self.lru[key]
            curr.val = value
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            curr.next = self.head.next
            curr.prev = self.head
            self.head.next = curr
            curr.next.prev = curr
        else:
            node = Node(key, value, None, None)
            node.prev = self.head
            node.next = self.head.next
            node.next.prev = node
            self.head.next = node
            self.lru[key] = node
            self.size += 1
        if self.size > self.cap:
            del_node = self.tail.prev
            del_node.prev.next = self.tail
            del_node.next.prev = del_node.prev
            del self.lru[del_node.key]
            del del_node
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)