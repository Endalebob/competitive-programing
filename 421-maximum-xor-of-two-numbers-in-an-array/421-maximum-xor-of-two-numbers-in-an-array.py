class Node:
    def __init__(self):
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,nums):
        num = format(nums,'b').zfill(32)
        curr = self.root
        for i in num:
            if i not in curr.child:
                curr.child[i] = Node()
            curr = curr.child[i]
    def find_max(self,nums):
        num = format(nums,'b').zfill(32)
        curr = self.root
        ans = ''
        for i in num:
            if i == '0':
                op = '1'
            else:
                op = '0'
            if op in curr.child:
                ans += op
                curr = curr.child[op]
            else:
                ans += i
                curr = curr.child[i]
        return int(ans,2) ^ nums
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for i in nums:
            trie.insert(i)
        ans = 0
        for i in nums:
            ans = max(ans,trie.find_max(i))
        return ans
        