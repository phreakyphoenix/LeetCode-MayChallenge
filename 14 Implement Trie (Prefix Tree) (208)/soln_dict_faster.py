from collections import defaultdict

class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False 

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root

        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]

        root.terminating = True

        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root

        for letter in word:
            if letter not in root.children:
                return False
            root = root.children[letter]

        return True if root.terminating else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root

        for letter in prefix:
            if letter not in root.children:
                return False
            root = root.children[letter]

        return True 
obj = Trie()
print (obj.insert("apple"))
print (obj.search("apple"))   # returns true
# print (obj.search("app"))    # returns false
print (obj.startsWith("app")) # returns true
# print (obj.insert("app"))   
# print (obj.search("app"))     # returns true