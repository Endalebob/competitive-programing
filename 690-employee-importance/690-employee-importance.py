"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp,id):
            i = 0
            for i in emp:
                if i.id == id:
                    self.ans += i.importance
                    break
            for j in i.subordinates:
                dfs(employees,j)
        self.ans = 0
        dfs(employees,id)
        return self.ans