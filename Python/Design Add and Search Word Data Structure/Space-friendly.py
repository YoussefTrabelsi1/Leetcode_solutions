# Length-bucketed WordDictionary
# - Keep words grouped by their length to avoid scanning irrelevant words
# - Space stays O(N) (no trie overhead), search is faster in mixed-length datasets

from collections import defaultdict

class WordDictionary:
    def __init__(self):
        self.buckets = defaultdict(list)  # length -> list of words of that length

    def addWord(self, word: str) -> None:
        self.buckets[len(word)].append(word)

    def search(self, pattern: str) -> bool:
        L = len(pattern)
        for w in self.buckets.get(L, ()):
            ok = True
            for pc, wc in zip(pattern, w):
                if pc != '.' and pc != wc:
                    ok = False
                    break
            if ok:
                return True
        return False


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
