# lru_bruteforce.py

class LRUCache:
    """
    Brute-force LRU using a Python list of (key, value) pairs.
    Recency is maintained by moving the touched pair to the end.
    Time: get/put = O(n) in worst-case (linear scan)
    Space: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []  # list of (key, value), LRU at index 0, MRU at end

    def _find_index(self, key):
        for i, (k, _) in enumerate(self.items):
            if k == key:
                return i
        return -1

    def get(self, key: int) -> int:
        idx = self._find_index(key)
        if idx == -1:
            return -1
        k, v = self.items.pop(idx)
        self.items.append((k, v))  # move to MRU
        return v

    def put(self, key: int, value: int) -> None:
        idx = self._find_index(key)
        if idx != -1:
            # update + move to MRU
            _k, _v = self.items.pop(idx)
            self.items.append((key, value))
            return
        # insert new
        if len(self.items) == self.capacity:
            self.items.pop(0)  # evict LRU
        self.items.append((key, value))  # as MRU

if __name__ == "__main__":
    # Example run from the prompt
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
