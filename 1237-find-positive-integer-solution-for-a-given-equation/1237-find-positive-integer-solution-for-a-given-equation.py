"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x = 1
        y = 1000
        while x<=1000 and customfunction.f(x,1) <= z:
            while y>0 and customfunction.f(x,y) > z:
                y -= 1
            if customfunction.f(x,y) == z:
                ans.append([x,y])
            x += 1
        return ans