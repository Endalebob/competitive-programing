class Node:
    def __init__(self):
        self.letters = [None] * 26
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        val_of_a = ord('a')
        current = self.root

        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                current.letters[letter] = Node()
            current = current.letters[letter]
        current.is_end = True

    def search(self,word):

        val_of_a = ord('a')
        current = self.root
        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                return False
            current = current.letters[letter]

        return current.is_end

    def startsWith(self,word):
        val_of_a = ord('a')
        current = self.root
        for letter in word:
            letter = ord(letter) - val_of_a
            if current.letters[letter] is None:
                return False
            current = current.letters[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)