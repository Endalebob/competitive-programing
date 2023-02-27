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
        self.ans = []
        self.initial = 0
        self.nest = nestedList
        # if self.nest.
        self.ans += self.rec(self.nest)
    def rec(self,nestedList):
        ans = []
        # else:
        for element in nestedList:
            if not element.isInteger():
                ans += self.rec(element.getList())
            else:
                ans += [element]
        return ans
            
    def next(self) -> int:
        temp = self.ans[self.initial]
        self.initial += 1
        return temp
    
    def hasNext(self) -> bool:
         return self.initial < len(self.ans)

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())