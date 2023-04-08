/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let memo = new Map()
    var dp = (idx)=>{
        if (idx === n){
            return 1;
        }
        if (idx > n){
            return 0;
        }
        if (memo.has(idx)){
            return memo.get(idx);
        }
        let tot = 0
        tot += dp(idx+1)
        tot += dp(idx+2)
        memo.set(idx,tot)
        return tot
    }
    return dp(0)
    
};