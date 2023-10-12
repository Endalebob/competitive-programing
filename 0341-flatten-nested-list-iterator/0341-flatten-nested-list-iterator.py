# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.NL = nestedList
        self.flat = []
        self.flatten(self.NL)
        self.idx = 0
        
    
    def next(self) -> int:
        ans = self.flat[self.idx]
        self.idx += 1
        return ans
    
    def hasNext(self) -> bool:
        return self.idx < len(self.flat)
         
    def flatten(self,val):
        if type(val) == type(1):
            return self.flat.append(val)
        if type(val) == type([1]):
            for i in val:
                self.flatten(i)
        else:
            if val.isInteger():
                self.flatten(val.getInteger())
            else:
                self.flatten(val.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())