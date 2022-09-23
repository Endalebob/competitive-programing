class WordDictionary:

    def __init__(self):
        self.root = [{},False];

    def addWord(self, word: str) -> None:
        curr = self.root;
        for i in word:
            if i not in curr[0]:
                curr[0][i] = [{},False]
            curr = curr[0][i]
        curr[1] = True

    def search(self, word: str) -> bool:
        def look(idx = 0,dsa = self.root):
            if idx == len(word):
                return dsa[1]
            ans = False
            if word[idx] == '.':
                for i in dsa[0]:
                    ans |= look(idx+1,dsa[0][i])
                    if ans:
                        break
            if word[idx] in dsa[0]:
                ans |= (look(idx+1,dsa[0][word[idx]]))
            return ans
        return look()


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)