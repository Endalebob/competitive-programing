class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vstd = set()
        def dfs(idx):
            vstd.add(idx)
            for i in rooms[idx]:
                if i not in vstd:
                    dfs(i)
        dfs(0)
        return len(vstd) == len(rooms)