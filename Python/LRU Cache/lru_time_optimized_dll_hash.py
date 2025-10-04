# lru_time_optimized_dll_hash.py

class LRUCache:
    """
    Classic O(1) LRU with a hashmap + doubly linked list (Node objects).
    Time: get/put average O(1)
    Space: O(capacity)
    """
    class _Node:
        __slots__ = ("key", "val", "prev", "next")
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> _Node
        # Sentinels
        self.head = self._Node()  # LRU side (head.next is least-recent)
        self.tail = self._Node()  # MRU side (tail.prev is most-recent)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- internal DLL ops ----
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_mru(self, node):
        # place node just before tail
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def _pop_lru(self):
        lru = self.head.next
        if lru is self.tail:
            return None
        self._remove(lru)
        return lru

    # ---- API ----
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_mru(node)
            return
        if len(self.map) == self.capacity:
            evicted = self._pop_lru()
            if evicted is not None:
                del self.map[evicted.key]
        node = self._Node(key, value)
        self.map[key] = node
        self._add_mru(node)

if __name__ == "__main__":
    ops = ["LRUCache", "put", "get", "put", "put", "get", "get"]
    args = [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]]
    out = [None]
    lru = LRUCache(*args[0])
    for op, ar in zip(ops[1:], args[1:]):
        if op == "put":
            lru.put(*ar)
            out.append(None)
        else:
            out.append(lru.get(*ar))
    print(out)  # [None, None, 10, None, None, 20, -1]
