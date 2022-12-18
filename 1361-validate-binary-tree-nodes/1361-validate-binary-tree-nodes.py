class Solution:
    def validateBinaryTreeNodes(self, n: int, lc: List[int], rc: List[int]) -> bool:
        tot = set(lc+rc)
        root = 0
        for i in range(n):
            if i not in tot:
                root = i
        deq = deque([root])
        vstd = set()
        while deq:
            curr = deq.popleft()
            if curr in vstd:
                return
            vstd.add(curr)
            if lc[curr]+1:
                deq.append(lc[curr])
            if rc[curr]+1:
                deq.append(rc[curr])
        return len(vstd) == n