# Brute-force WordDictionary
# - Store every word in a simple list (O(N) space)
# - Search by scanning all words and checking character-by-character (O(N * L))

class WordDictionary:
    def __init__(self):
        self.words = []  # list of strings

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, pattern: str) -> bool:
        L = len(pattern)
        for w in self.words:
            if len(w) != L:
                continue
            # match pattern to w
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
    outputs = [None]  # constructor returns null/None
    wd.addWord("day"); outputs.append(None)
    wd.addWord("bay"); outputs.append(None)
    wd.addWord("may"); outputs.append(None)
    outputs.append(wd.search("say"))  # False
    outputs.append(wd.search("day"))  # True
    outputs.append(wd.search(".ay"))  # True
    outputs.append(wd.search("b.."))  # True
    print(outputs)  # [None, None, None, None, False, True, True, True]
