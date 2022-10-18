# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        m,n = n,m
        matrix = [[-1 for col in range(m)] for row in range(n)]
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        isvalid = lambda r,c : 0<=r<n and 0<=c<m and matrix[r][c] == -1 
        matrix[0][0] = head.val
        head = head.next
        r,c = 0,0
        n_squer = n*m-1
        
        while head and n_squer:
            for dr,dc in directions:
                while head and isvalid(r+dr,c+dc):
                    r += dr
                    c += dc
                    matrix[r][c] = head.val
                    n_squer -= 1
                    head = head.next
        return matrix