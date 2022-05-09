class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],
            '5': ['j','k','l'],'6': ['m','n','o'],'7': ['p','q','r','s'],
            '8': ['t','u','v'],'9': ['w','x','y','z']}
        hold = {}
        def backtrack(idx):
            if idx in hold:
                return hold[idx]
            if idx == len(digits)-1:
                hold[idx] = dic[digits[idx]]
                return dic[digits[idx]]
            val = []
            for i in dic[digits[idx]]:
                temp = backtrack(idx+1)
                for j in temp:
                    val.append(i+j)
            hold[idx] = val
            return val
        if len(digits) == 0:
            return []
        return backtrack(0)
            
            