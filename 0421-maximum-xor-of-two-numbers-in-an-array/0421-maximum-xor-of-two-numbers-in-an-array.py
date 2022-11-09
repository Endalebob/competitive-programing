class Node:
    def __init__(self):
        self.letters = {}
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        word = format(word,'b').zfill(32)
        current = self.root
        for bit in word:
            if  bit not in current.letters:
                current.letters[bit] = Node()
            current = current.letters[bit]
    def find(self,word):
        words = format(word,'b').zfill(32)
        current = self.root
        ret = ''
        for bit in words:
            if bit == '0':
                op = '1'
            else:
                op = '0'
            if op in current.letters:
                ret += op
                current = current.letters[op]
            else:
                ret+= bit
                current = current.letters[bit]
        return int(ret,2) ^ word
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for i in nums:
            trie.insert(i)
        ans = 0
        for i in nums:
            ans = max(ans,trie.find(i))
        return ans
        