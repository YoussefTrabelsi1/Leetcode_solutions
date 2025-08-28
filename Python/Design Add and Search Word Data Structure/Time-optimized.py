# Trie-based WordDictionary (time-optimized)
# - Insert: O(L)
# - Search: average O(L) with branching only when encountering '.'
# - Typically much faster than scanning, at the expense of extra memory

class TrieNode:
    __slots__ = ("next", "end")
    def __init__(self):
        self.next = {}    # char -> TrieNode
        self.end = False  # end-of-word marker

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = TrieNode()
            node = node.next[ch]
        node.end = True

    def search(self, pattern: str) -> bool:
        # DFS over trie to support '.'
        def dfs(i: int, node: TrieNode) -> bool:
            if i == len(pattern):
                return node.end
            ch = pattern[i]
            if ch == '.':
                for child in node.next.values():
                    if dfs(i + 1, child):
                        return True
                return False
            if ch in node.next:
                return dfs(i + 1, node.next[ch])
            return False

        return dfs(0, self.root)


# --- Demo (reproduces example) ---
if __name__ == "__main__":
    wd = WordDictionary()
    outputs = [None]
    wd.addWord("day"); outputs.append(None)
    wd.addWord("bay"); outputs.append(None)
    wd.addWord("may"); outputs.append(None)
    outputs.append(wd.search("say"))  # False
    outputs.append(wd.search("day"))  # True
    outputs.append(wd.search(".ay"))  # True
    outputs.append(wd.search("b.."))  # True
    print(outputs)  # [None, None, None, None, False, True, True, True]
