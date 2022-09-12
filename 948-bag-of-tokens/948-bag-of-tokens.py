class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        j,i = len(tokens)-1,0
        while i<=j:
            if tokens[i]<=power:
                score += 1
                power -= tokens[i]
                i += 1
            elif i<j and score>0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return score