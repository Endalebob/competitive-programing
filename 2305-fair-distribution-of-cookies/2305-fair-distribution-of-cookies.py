class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0]*k
        self.ans = float('inf')
        def bact(idx,cnt):
            if len(cookies)-idx < cnt:
                return
            if idx == len(cookies):
                self.ans = min(self.ans,max(dist))
                return
            for j in range(k):
                cnt -= dist[j] == 0
                dist[j] += cookies[idx]
                bact(idx+1,cnt)
                dist[j] -= cookies[idx]
                cnt += dist[j] == 0
        bact(0,k)
        return self.ans