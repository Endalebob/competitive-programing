Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ans(nums,l,r):
    r_sum = nums[r]
    l_sum = nums[l]
    while l<r-1:
        if len(nums)-r>l:
            l += 1
            l_sum += nums[l]
        elif r_sum<=l_sum:
            r -= 1
            r_sum += nums[r]
        if r_sum>l_sum and len(nums)-r<=l:
            return 'YES'
        
    return 'NO'
no_test = int(input())
for i in range(no_test):
    length = int(input())
    r = length - 1
    l = 0
    nums = list(map(int,input().split()))
    nums.sort()
    print(ans(nums,l,r))