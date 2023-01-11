class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def build(idx):
            add = '_'*idx
            rem = 0
            ret = []
            for i in range(1,10**idx):
                create = '<' + str(i) + '/' + add + '>'
                val = limit - len(create)
                if val < 1:
                    return []
                take = message[rem:rem+val] + create
                ret.append(take)
                rem += val
                if rem >= len(message):
                    return ret
            if rem < len(message):
                return []
        for i in range(1,5):
            lis = build(i)
            if lis:
                ans = []
                c = len(lis)
                for ii in range(c):
                    s = lis[ii][:-i-1] + str(c) + '>'
                    ans.append(s)
                return ans
                    