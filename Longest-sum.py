Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(int(input())):
    a = int(input())
    ans = 0
    nums = list(map(int,input().split()))
    dp = [0]*a
    for j in range(a-1,-1,-1):
        if j+nums[j]<a:
            dp[j] = nums[j] + dp[nums[j]+j]
        else:
            dp[j] = nums[j]
        ans = max(ans,dp[j])
    print(ans)