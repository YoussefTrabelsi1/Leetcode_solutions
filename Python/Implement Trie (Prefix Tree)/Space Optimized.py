class PrefixTree:
    def __init__(self):
        self.word_set = set()

    def insert(self, word: str) -> None:
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        for w in self.word_set:
            if w.startswith(prefix):
                return True
        return False
