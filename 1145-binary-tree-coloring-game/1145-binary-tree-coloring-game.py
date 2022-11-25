class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def dfs_with_root(root):
            if not root:
                return 0
            return dfs_with_root(root.left) + dfs_with_root(root.right) + 1
        dfs_with = [root]
        def dfs_with_out_root(root):
            if not root:
                return 0
            if root.val == x:
                dfs_with[0] = root
                return -1
            return dfs_with_out_root(root.left) + dfs_with_out_root(root.right) + 1
        with_root = 0
        with_out_root = dfs_with_out_root(root)+1
        if dfs_with[0].left:
            with_root = max(with_root,dfs_with_root(dfs_with[0].left),dfs_with_root(dfs_with[0].right))
        
        
        return max(with_out_root,with_root) > n//2
                    