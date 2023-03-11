class Solution:
    def printVertically(self, s: str) -> List[str]:
        list_s = s.split()
        ans = []
        flag = True
        curr_idx = 0
        while flag:
            temp = ''
            flag = False
            for i in list_s:
                if len(i) > curr_idx:
                    temp += i[curr_idx]
                    flag = True
                else:
                    temp += ' '
            if flag:
                ans.append(temp.rstrip())
            curr_idx += 1
        return ans
                    