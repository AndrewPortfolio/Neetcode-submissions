class PrefixTree:
    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        if word in self.words: return True

        return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.words:
            if prefix == s[:len(prefix)]: 
                return True
        return False
        