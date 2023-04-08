/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b) => a-b)
    const ans = []
    for (let i=0;i<nums.length-2;i++){
        if (i>0){
            if(nums[i] == nums[i-1]){
                continue
            }
        }
        let curr = nums[i];
        let l = i+1;
        let r = nums.length - 1
        while (l<r){
            let val = nums[l] + nums[r] + curr
            if (val === 0){
                    ans.push([curr,nums[l],nums[r]]);
                const t = nums[r];
                while (r>l && t === nums[r]){
                    r -= 1
                }
            }
            else if(val<0){
                l += 1;
            }
            else{
                r -= 1;
            }
        }
    }
    return ans
    
};