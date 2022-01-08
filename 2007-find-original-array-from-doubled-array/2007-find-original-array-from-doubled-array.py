class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = []
        dic = {} 
        leen = len(changed)//2
        if len(changed)%2 != 0:
            return []
        original = [0]*(changed.count(0)//2)
        for i in changed:
            if i != 0:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
        for i in dic:
            if dic[i]<1:
                continue
            if 2*i not in dic:
                return []
            else:
                if dic[2*i]>= dic[i]:
                    dic[2*i] -= dic[i]
                    for m in range(dic[i]):
                        original.append(i)
                else:
                    return []
            if len(original)>= leen:
                return original
        return original
        