
class Trie:
    def __init__(self):
        self.letters = {}
        self.is_end = False
    def insert(self,word):
        current = self

        for letter in word:
            if letter not in current.letters:
                current.letters[letter] = Trie()
            current = current.letters[letter]
        current.is_end = True

    def search(self,word):

        val_of_a = ord('a')
        current = self
        for letter in word:
            if letter not in current.letters:
                return False
            current = current.letters[letter]

        return current.is_end

    def startsWith(self,word):
        current = self
        for letter in word:
            if letter not in current.letters:
                return False
            current = current.letters[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)