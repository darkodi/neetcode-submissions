class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# cache contains key -> node mapping
# nodes are linked in a doubly linked list because of O(1) add/remove operations
# head and tail are dummy nodes to simplify add/remove operations
# helper functions: add_front(node), remove(node)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: int -> value: node
        # head points to the most recently used node
        self.head = Node(0, 0) # dummy head
        # tail points to the least recently used node
        self.tail = Node(0, 0) # dummy tail
        # link head and tail in doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node: Node) -> None:
        # detach the node from the list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_front(self, node: Node) -> None:
        # add the node to the front of the list (right after head)
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        

    def get(self, key: int) -> int:
        # if key does not exist, return -1
        if key not in self.cache:
            return -1
        # key exists, move the node to the front of the list and return its value
        node = self.cache[key]
        self.remove(node) # detach it from the list
        self.add_front(node) # add to the front of the list
        return node.value

    def put(self, key: int, value: int) -> None:
        # if the key does exist, remove the old node, add the new node to the front and return
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # detach it from the list
            # update the value
            node.value = value
            self.add_front(node) # add to the front of the list
            return
        # the key does not exist 
        node = Node(key, value)
        self.cache[key] = node # point to the new node
        self.add_front(node) # add to the front of the list

        # If the cache exceeds capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev # the node to be removed
            self.remove(lru_node) # detach it from the list
            del self.cache[lru_node.key] # remove it from the cache
        
