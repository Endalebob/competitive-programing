class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        def perm(idx,new_s):
            if idx == len(s):
                output.append(new_s)
                return
            if s[idx].isdigit():
                perm(idx+1,new_s+s[idx])
            else:
                lowwer,upper = s[idx].lower(),s[idx].upper()
                perm(idx+1,new_s+lowwer)
                perm(idx+1,new_s+upper)
        perm(0,'')
        return output