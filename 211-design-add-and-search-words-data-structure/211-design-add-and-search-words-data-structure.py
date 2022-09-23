class WordDictionary:

    def __init__(self):
        self.trie = [{  }, False];

    def addWord(self, word: str) -> None:
        c = self.trie;

        for letter in word:
            if letter not in c[0]:
                c[0][letter] = [{  }, False];
            
            c = c[0][letter];
        
        c[1] = True;

    def search(self, word: str) -> bool:
        
        def go(node=self.trie, x=0):
            if x == len(word):
                return node[1];
            
            ans = False;
            if word[x] == '.':
                for childKey, childData in node[0].items():
                    ans |= go(childData, x+1);
                    if ans: break;
            elif word[x] in node[0]:
                ans |= go(node[0][word[x]], x+1);

            return ans;
        
        return go();