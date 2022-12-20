class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vstd = set()
        def dfs(key):
            if key in vstd: return
            vstd.add(key)
            for i in rooms[key]: dfs(i)
        dfs(0)
        return len(vstd) == len(rooms)