class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        pref = defaultdict(int)
        for i,j in flowers:
            pref[i] += 1
            pref[j+1] -= 1
        key = sorted(pref.keys())
        curr = 0
        for i in key:
            curr += pref[i]
            pref[i] = curr
        ans = []
        for i in persons:
            if i > key[-1]:
                ans.append(0)
                continue
            idx = bisect_left(key,i)
            if key[idx] == i:
                
                ans.append(pref[key[idx]])
            else:
                ans.append(pref[key[idx-1]])
        return ans
                            