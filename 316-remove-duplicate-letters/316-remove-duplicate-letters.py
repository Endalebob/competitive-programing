class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        monstack = []
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        check = set()
        for i in s:
            dic[i] -= 1
            if i in check:
                continue
            while monstack and monstack[-1]>i and dic[monstack[-1]]>0:
                popped = monstack.pop()
                check.remove(popped)
            check.add(i)
            monstack.append(i)
        return ''.join(monstack)
            