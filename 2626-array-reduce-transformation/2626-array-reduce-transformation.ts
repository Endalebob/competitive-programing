type Fn = (accum: number, curr: number) => number

const reduce = (nums: number[], fn: Fn, init: number): number =>{
    let ans = init
    for (let i=0;i<nums.length; i++){
        ans = fn(ans,nums[i])
    }
    return ans

};