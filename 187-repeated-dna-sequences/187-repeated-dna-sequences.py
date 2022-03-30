class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<11:
            return None
        ans,r = [],10
        deq = ''
        dic = {}
        for i in range(r):
            deq += s[i]
        dic[deq] = 1
        temp = deq
        while r<len(s):
            temp = temp[1:]
            temp+= s[r]
            if temp in dic:
                dic[temp] += 1
                if dic[temp]==2:
                    ans.append(temp)
            else:
                dic[temp] = 1
            r += 1
        return ans
            