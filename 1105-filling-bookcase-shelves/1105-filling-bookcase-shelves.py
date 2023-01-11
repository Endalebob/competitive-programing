class Solution:
    def minHeightShelves(self, books: List[List[int]], sw: int) -> int:
        @lru_cache(None)
        def dp(idx,spot,maxi):
            if idx == len(books):
                return maxi
            if spot == 0:
                return dp(idx+1,spot+books[idx][0],max(maxi,books[idx][1]))
            elif spot + books[idx][0] <= sw:
                return min(dp(idx+1,spot+books[idx][0],max(maxi,books[idx][1])),maxi + dp(idx+1,books[idx][0],books[idx][1]))
            return maxi + dp(idx+1,books[idx][0],books[idx][1])
        return dp(0,0,0)