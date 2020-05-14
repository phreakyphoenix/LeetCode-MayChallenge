class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        root = self.trie
        for c in word:
            if c not in root:
                root[c]={}
            root = root[c]
        root['#'] = '#'

    def search(self, word: str) -> bool:
        # start = self.trie
        # for c in word:
        #     if c not in start:
        #         return False
        #     start = start[c]
        # if '#' in start:
        #     return True
        # return False
        return self.startsWith(word + '#')

    def startsWith(self, prefix: str) -> bool:
        start = self.trie
        for c in prefix:
            if c not in start:
                return False
            start = start[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)