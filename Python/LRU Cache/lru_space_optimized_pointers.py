# lru_space_optimized_pointers.py

class LRUCache:
    """
    Space-optimized LRU without Node objects.
    We keep:
      - store: key -> [value, prev_key, next_key]
      - Two sentinels represented by special keys: HEAD=None (LRU side), TAIL="__TAIL__"
    Links are by keys to avoid per-node class overhead.
    Time: get/put average O(1)
    Space: O(capacity) with compact per-key lists
    """
    __TAIL__ = "__TAIL_SENTINEL__"

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}  # key -> [value, prev_key, next_key]
        # doubly-linked list via keys
        self.head = None            # HEAD sentinel key
        self.tail = self.__TAIL__   # TAIL sentinel key
        # Sentinels live in store with pointers only; HEAD.next is first real (LRU), TAIL.prev is MRU
        self.store[self.head] = [None, None, self.tail]    # [value(None), prev(None), next]
        self.store[self.tail] = [None, self.head, None]    # [value(None), prev, next(None)]

    # ---- internal DLL ops (by key) ----
    def _unlink(self, key):
        val, prev_k, next_k = self.store[key]
        # connect neighbors
        self.store[prev_k][2] = next_k
        self.store[next_k][1] = prev_k

    def _append_mru(self, key):
        # Insert just before tail (MRU position)
        tail_prev = self.store[self.tail][1]
        self.store[key][1] = tail_prev
        self.store[key][2] = self.tail
        self.store[tail_prev][2] = key
        self.store[self.tail][1] = key

    def _pop_lru_key(self):
        first = self.store[self.head][2]
        if first == self.tail:
            return None
        self._unlink(first)
        return first

    # ---- API ----
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        if key in (self.head, self.tail):
            return -1
        self._unlink(key)
        self._append_mru(key)
        return self.store[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key][0] = value
            self._unlink(key)
            self._append_mru(key)
            return
        if len(self.store) - 2 == self.capacity:  # exclude 2 sentinels
            evict = self._pop_lru_key()
            if evict is not None:
                del self.store[evict]
        # insert new key at MRU
        self.store[key] = [value, None, None]
        self._append_mru(key)

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
