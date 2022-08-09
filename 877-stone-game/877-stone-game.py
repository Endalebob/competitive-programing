class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(turn,l,r,alice,bob):
            if l > r:
                return alice > bob
            if (turn,l,r) in memo:
                return memo[(turn,l,r)]
            if turn == 0:
                if dp(1-turn,l+1,r,alice+piles[l],bob):
                    memo[(turn,l,r)] = True
                    return True
                if dp(1-turn,l,r-1,alice+piles[r],bob):
                    memo[turn,l,r] = True
                    return True
            else:
                if dp(1-turn,l+1,r,alice,piles[l]+bob):
                    memo[turn,l,r] = True
                    return True
                if dp(1-turn,l,r-1,alice,piles[r]+bob):
                    memo[turn,l,r] = True
                    return True
            memo[(turn,l,r)] = False
            return False
        return dp(0,0,len(piles)-1,0,0)
            