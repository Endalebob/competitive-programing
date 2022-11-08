# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #first i need to know the left and right most element for every depth
        #for root depth = 0 right = left =0
        # can be expressed {depth : [left:right]}
        dic = {}
        def dfs(r,depth,pos):
            if not r:
                return
            if depth in dic:
                dic[depth][0] = min(dic[depth][0],pos)
                dic[depth][1] = max(dic[depth][1],pos)
            else:
                dic[depth] = [pos,pos]
            
            dfs(r.left,depth+1,2*pos)
            dfs(r.right,depth+1,2*pos+1)
        dfs(root,0,0)
        ans = 0
        for i in dic:
            ans = max(ans,dic[i][1] - dic[i][0]+1)
        return ans
            