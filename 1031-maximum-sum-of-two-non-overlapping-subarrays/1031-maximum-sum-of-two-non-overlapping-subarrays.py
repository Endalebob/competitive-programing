class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        store1 = []
        maxx = firstLen-1
        minn = 0
        val = 0
        for i in range(firstLen):
            val += nums[i]
        for i in range(len(nums)-firstLen):
            store1.append([minn,maxx,val])
            val -= nums[minn]
            minn += 1
            maxx += 1
            val += nums[maxx]
        store1.append([minn,maxx,val])
        store2 = []
        maxx = secondLen-1
        minn = 0
        val = 0
        for i in range(secondLen):
            val += nums[i]
        for i in range(len(nums)-secondLen):
            store2.append([minn,maxx,val])
            val -= nums[minn]
            minn += 1
            maxx += 1
            val += nums[maxx]
        store2.append([minn,maxx,val])
        ans = 0
        for i in range(len(store1)):
            for j in range(len(store2)):
                if store1[i][1]<store2[j][0] or store1[i][0]>store2[j][1]:
                    ans = max(ans,store1[i][2] + store2[j][2])
        return ans