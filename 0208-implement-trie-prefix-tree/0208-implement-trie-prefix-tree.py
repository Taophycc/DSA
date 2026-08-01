class Trie:
    def __init__(self):
        self.root = self
        self.children = [None] * 26
        self.isLeaf = False

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                new_node = Trie()
                curr.children[index] = new_node
            curr = curr.children[index]
        curr.isLeaf = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)