def printing_nodes(head, tail, kv_dict):
    curr_node = head.next
    while curr_node != tail:
        print(f"key {curr_node.key}: value {curr_node.value}")
        curr_node = curr_node.next
    printing_dict(kv_dict)
def printing_dict(kv_dict):
    #print(kv_dict.items())
    for k, v in kv_dict.items():
        print(f"mainline print of dict key {k}: value {v.value}")


class Node:
    def __init__(self, k, v, prev, next):
        self.key = k
        self.value = v
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Incorrect Capacity")
        self.kv_dict = {}
        self.capacity = capacity
        self.curr = 0
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, None, None)
        

    def get(self, key: int) -> int:
        #print(f"in get key = {key}")
        #printing_nodes(self.head, self.tail, self.kv_dict)
        if self.kv_dict.get(key, -1) != -1:
            #print(self.kv_dict.get(key).value)
            self._move_to_front(key, new=False)
            return self.kv_dict.get(key).value
        return -1

    def put(self, key: int, value: int) -> None:
        if not self.kv_dict:
            new_node = Node(key, value, self.head, self.tail)
            self.kv_dict[key] = new_node
            self.head.next = new_node
            self.tail.prev = new_node
            self.curr += 1

        elif key in self.kv_dict:
            self.kv_dict[key].value = value
            self._move_to_front(key, new=False)
            #print(key, self.kv_dict[key].value, "yippie")
            #printing_dict(self.kv_dict)
        else:
            key_node = Node(key, value, None, None)
            self.kv_dict[key] = key_node
            self._move_to_front(key, new=True)
            self.curr += 1

            if self.curr > self.capacity:
                #remove from node stream, then remove from dict
                temp = self.tail.prev
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
                del self.kv_dict[temp.key]
                del temp
                self.curr -= 1

        #printing_nodes(self.head, self.tail, self.kv_dict)
        return 
    
    def _move_to_front(self, k, new):
        curr_node = self.kv_dict[k]
        if not new: #removes node from the stream
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        if self.head.next != curr_node: #rewrites head of stream to include node
                curr_node.next = self.head.next
                self.head.next.prev = curr_node
                self.head.next = curr_node
                curr_node.prev = self.head

        
        

    
