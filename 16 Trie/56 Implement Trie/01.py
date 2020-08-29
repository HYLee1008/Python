### Implement trie methods (insert, search, startsWith) using dictionary
###
import collections


# Node of trie
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # Check word existence
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # Check word existance using string
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
