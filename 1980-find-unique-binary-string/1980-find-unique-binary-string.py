class Trie:
    def __init__(self):
        self.letter = {}
        self.isend = False
    def insert(self,num):
        current = self
        for i in num:
            if i not in current.letter:
                current.letter[i] = Trie()
            current = current.letter[i]
        current.end = True
    
    def find(self,num):
        current = self
        for i in range(len(num)):
            val = str(1-int(num[i]))
            if val not in current.letter:
                return True,i
            current = current.letter[num[i]]
        return False,0
            
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        trie = Trie()
        for i in nums:
            trie.insert(i)
        for i in nums:
            t_or_f, idx = trie.find(i)
            if t_or_f:
                num = list(i)
                num[idx] = str(1-int(num[idx]))
                return ''.join(num)
        