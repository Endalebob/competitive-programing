class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # this is siliding window problem
        # window size = k
        count_black = 0
        for i in range(k):
            if blocks[i] == 'B':
                count_black += 1
        ans = k-count_black
        for i in range(k,len(blocks)):
            if blocks[i] == 'B':
                count_black +=1
            if blocks[i-k] == 'B':
                count_black -= 1
            ans = min(ans,k-count_black)
        return ans