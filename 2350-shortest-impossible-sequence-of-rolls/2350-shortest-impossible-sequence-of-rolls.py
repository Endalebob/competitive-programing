class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1
        unique = set()
        for i in rolls:
            prev = len(unique)
            unique.add(i)
            if prev < len(unique):
                if len(unique) == k:
                    ans += 1
                    unique = set()
        return ans